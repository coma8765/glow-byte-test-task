from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.models import Reservation, User
from src.modules.api.depends.reservation_service import get_reservation_service
from src.modules.api.depends.user import get_user
from src.modules.api.services.reservations.reservations import (
    ReservationService,
    HotelNotFound,
    InvalidDate,
)

router = APIRouter()


class ReservationRef(BaseModel):
    hotelUid: UUID
    startDate: datetime
    endDate: datetime


@router.post("/")
async def create_reservation(
    ref: ReservationRef,
    user: User = Depends(get_user),
    service: ReservationService = Depends(get_reservation_service),
):
    try:
        return service.create(
            Reservation(
                user_uid=user.user_uid,
                hotel_uid=ref.hotelUid,
                start_date=ref.startDate,
                end_date=ref.endDate,
            )
        )
    except InvalidDate:
        raise HTTPException(
            status_code=422, detail="date cannot be in the past"
        )
    except HotelNotFound:
        raise HTTPException(status_code=404, detail="hotel does not exist")
