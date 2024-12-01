import time
import mlflow
import torch
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from app.entities.stock import StockPriceDTO, HistoricalStockPricesDTO
from app.utils.lstm import StockLSTM


class StockPriceForecaster:

    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.stock_lstm = StockLSTM()
        self.model = self.stock_lstm.get_model()

    def execute(self, historical_prices: HistoricalStockPricesDTO) -> float:
        price_predict = self.__predict(historical_prices.prices)
        return price_predict

    def __predict(self, prices: list[float]) -> float:
        mlflow.set_experiment("Stock Price Prediction API")
        input_data = np.array(prices).reshape(-1, 1)
        scaled_data = self.scaler.fit_transform(input_data)
        input_tensor = torch.tensor(scaled_data, dtype=torch.float32).unsqueeze(0)

        start_time = time.time()

        with torch.no_grad():
            prediction_scaled = self.model(input_tensor).item()

        end_time = time.time()
        response_time = end_time - start_time
        prediction = self.scaler.inverse_transform([[prediction_scaled]])[0][0]

        with mlflow.start_run(run_name="Prediction Monitoring"):
            mlflow.log_param("input_prices", prices)
            mlflow.log_metric("response_time", response_time)
            mlflow.log_metric("predicted_price", prediction)

        return float(prediction)
