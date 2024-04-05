from uuid import UUID

from src.datasources import HotelSource, ReservationSource, UserSource
from src.models import Reservation, User
from src.modules.api.services.exc import InvalidData, NotFound


class InvalidDate(InvalidData):
    pass


class HotelNotFound(NotFound):
    pass


class ReservationNotFound(NotFound):
    pass


class ReservationService:
    __slots__ = ("source", "user_source", "hotel_source", "user")

    user: User

    source: ReservationSource
    user_source: UserSource
    hotel_source: HotelSource

    def __init__(
        self,
        user: User,
        source: ReservationSource,
        user_source: UserSource,
        hotel_source: HotelSource,
    ):
        self.user = user

        self.source = source
        self.user_source = user_source
        self.hotel_source = hotel_source

    def create(self, reservation: Reservation) -> Reservation:
        """Creates a new reservation

        :raise InvalidDate: if start_date >= end_date
        :param reservation: Reservation data
        :returns: Reservation after processing
        """

        if reservation.start_date < reservation.end_date:
            raise InvalidDate()

        try:
            hotel = self.hotel_source.get_by_uid(reservation.hotel_uid)
        except self.hotel_source.errors.hotelNotFound:
            raise HotelNotFound(reservation.hotel_uid)

        reservation_timedelta = reservation.end_date - reservation.start_date

        reservation.cost = hotel.price
        reservation.cost *= reservation_timedelta.days
        reservation.cost *= 1 - self.user.loyalty.status.discount

        self.source.save(reservation)

        return reservation

    def cancel(self, reservation_uid: UUID):
        """Cancels a reservation

        :raise ReservationNotFound: id reservation not found
        :param reservation_uid:
        """
        try:
            reservation = self.source.get_by_uid(reservation_uid)
        except self.source.errors.reservationNotFound:
            raise ReservationNotFound(reservation_uid)

        reservation.status = reservation.status.CANCELED

        self.source.save(reservation)
