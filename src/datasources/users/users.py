from abc import ABC, abstractmethod
from uuid import UUID

from src.datasources.exc import NotFound
from src.models import User


class UserNotFound(NotFound):
    pass


class UserSource(ABC):
    """User data source

    :raise UserNotFound: If a reservation doesn't exist
    """

    __slots__ = ()

    @abstractmethod
    def get_by_uid(self, user_uid: UUID) -> User:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
