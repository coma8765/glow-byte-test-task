from abc import ABC, abstractmethod
from uuid import UUID

from src.datasources.exc import NotFound
from src.models import Hotel


class HotelNotFound(NotFound):
    pass


class _Errors:
    __slots__ = ()

    hotelNotFound = HotelNotFound()


class HotelSource(ABC):
    """Hotel data source

    :raise HotelNotFound: If a reservation doesn't exist
    """

    __slots__ = ()

    @abstractmethod
    def get_by_uid(self, user_uid: UUID) -> Hotel:
        pass

    @abstractmethod
    def save(self, hotel: Hotel) -> None:
        pass

    errors = _Errors()
