from fastapi import APIRouter

from app.services.stock_price_forecaster import StockPriceForecaster
from app.entities.stock import StockPriceDTO, HistoricalStockPricesDTO

router = APIRouter(prefix='/stocks')
stock_price_forecaster = StockPriceForecaster()


@router.post('/predict/close',
             description='Recebe uma lista de valores históricos de fechamento de uma ação da B3 e'
                         ' prevê o próximo valor de fechamento.')
def predict_close_price(prices_dto: HistoricalStockPricesDTO) -> StockPriceDTO:
    return stock_price_forecaster.execute(prices_dto)
