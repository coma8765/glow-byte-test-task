from enum import StrEnum, Enum

from pydantic import BaseModel


class LoyaltyStatus(Enum):
    BRONZE = "BRONZE", 0.5
    SILVER = "SILVER", 0.7
    GOLD = "GOLD", 0.10

    _discount: float

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, discount: float = None) -> None:
        self._discount = discount

    @property
    def discount(self) -> float:
        return self._discount


DEFAULT_LOYALTY_STATUS = LoyaltyStatus.BRONZE


class Loyalty(BaseModel):
    number_reservations: int = 0
    status: LoyaltyStatus = DEFAULT_LOYALTY_STATUS
