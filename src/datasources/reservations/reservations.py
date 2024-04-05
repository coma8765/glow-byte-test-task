from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from src.datasources.exc import NotFound
from src.models import Reservation


class ReservationNotFound(NotFound):
    pass


class _Errors:
    reservationNotFound = ReservationNotFound()


class ReservationSource(ABC):
    """Reservation data source

    :raise ReservationNotFound: If a reservation doesn't exist
    """

    __slots__ = ()

    @abstractmethod
    def get_by_uid(self, reservation_uid: UUID) -> Reservation:
        pass

    @abstractmethod
    def save(self, reservation: Reservation) -> None:
        pass

    errors = _Errors()
