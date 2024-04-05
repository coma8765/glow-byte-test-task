from fastapi import Depends

from src.datasources import HotelSource, UserSource, ReservationSource
from src.models import User
from src.modules.api.depends.user import get_user
from src.modules.api.services.reservations.reservations import (
    ReservationService,
)


def get_reservation_service(
    user: User = Depends(get_user),
    source: ReservationSource = Depends(),
    user_source: UserSource = Depends(),
    hotel_source: HotelSource = Depends(),
):
    return ReservationService(
        user=user,
        source=source,
        user_source=user_source,
        hotel_source=hotel_source,
    )
