from datetime import datetime
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ReservationStatus(StrEnum):
    SUCCESS = "SUCCESS"
    CANCELED = "CANCELED"


class Reservation(BaseModel):
    reservation_uid: UUID = Field(..., default_factory=uuid4)

    user_uid: UUID = Field(...)
    hotel_uid: UUID = Field(...)

    status: ReservationStatus = ReservationStatus.SUCCESS

    start_date: datetime = Field(
        ..., default_factory=lambda: datetime.now(tz=None)
    )
    end_date: datetime = Field(
        ..., default_factory=lambda: datetime.now(tz=None)
    )

    cost: int = Field(..., description="cost in kopeck", gt=0)
