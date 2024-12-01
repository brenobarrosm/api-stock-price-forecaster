from app.entities.stock import StockPriceDTO, HistoricalStockPricesDTO


class StockPriceForecaster:

    def execute(self, historical_prices: HistoricalStockPricesDTO) -> StockPriceDTO:
        return StockPriceDTO(close_price=0)
