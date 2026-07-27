from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class VehicleRatingCreate(BaseModel):

    vehicle_id: int

    user_id: Optional[int] = None

    rating: int = Field(
        ...,
        ge=1,
        le=5,
        description="Rating must be between 1 and 5 stars"
    )

    title: Optional[str] = None

    review_text: Optional[str] = None

    rating_type: Optional[str] = None

    source: Optional[str] = None

    status: Optional[str] = "Active"



class VehicleRatingResponse(BaseModel):

    id: int

    vehicle_id: int

    user_id: Optional[int]

    rating: int

    title: Optional[str]

    review_text: Optional[str]

    rating_type: Optional[str]

    source: Optional[str]

    status: str

    created_at: datetime


    class Config:
        from_attributes = True