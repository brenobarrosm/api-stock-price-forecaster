from typing import List

from app.utils.pydantic_config import ConfiguredBaseModel


class StockPriceDTO(ConfiguredBaseModel):
    close_price: float


class HistoricalStockPricesDTO(ConfiguredBaseModel):
    prices: List[float]
