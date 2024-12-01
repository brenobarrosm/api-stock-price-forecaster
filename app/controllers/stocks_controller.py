from fastapi import APIRouter, HTTPException

from app.services.stock_price_forecaster import StockPriceForecaster
from app.entities.stock import StockPriceDTO, HistoricalStockPricesDTO

router = APIRouter(prefix='/stocks')
stock_price_forecaster = StockPriceForecaster()


@router.post('/predict/close',
             description='Recebe uma lista de valores históricos de fechamento de uma ação da B3 e'
                         ' prevê o próximo valor de fechamento.')
def predict_close_price(prices_dto: HistoricalStockPricesDTO) -> StockPriceDTO:
    sequence_length = 15
    if len(prices_dto.prices) != sequence_length:
        raise HTTPException(
            status_code=400,
            detail=f'A entrada deve conter dados históricos de {sequence_length} dias exatamente.'
        )
    stock_price_predict = stock_price_forecaster.execute(prices_dto)
    return StockPriceDTO(close_price=stock_price_predict)
