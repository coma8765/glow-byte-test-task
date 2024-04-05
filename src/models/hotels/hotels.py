from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Hotel(BaseModel):
    hotel_uid: UUID = Field(..., default_factory=uuid4)
    title: str = Field(..., max_length=250)
    address: str = Field(..., max_length=250)
    price: int = Field(..., description="price in kopeck", gt=0)
