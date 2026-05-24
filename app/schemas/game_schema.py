"""
Schemas de resposta da API.
"""

from typing import Optional

from pydantic import BaseModel


class GameResponse(BaseModel):
    id: int
    name: str
    discount_percent: int
    original_price: float
    final_price: float
    currency: str
    windows_available: bool
    mac_available: bool
    linux_available: bool
    controller_support: Optional[str] = None


class StatsResponse(BaseModel):
    total_games: int
    average_discount: float
    highest_discount: int
    cheapest_price: float
    average_price: float
