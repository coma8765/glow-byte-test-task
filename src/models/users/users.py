from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from src.models.loyalty.loyalty import Loyalty


class User(BaseModel):
    user_uid: UUID = Field(..., default_factory=uuid4)
    username: str = Field(..., max_length=50)
    loyalty: Loyalty = Field(..., default_factory=Loyalty)
