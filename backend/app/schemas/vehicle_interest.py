from pydantic import BaseModel
from typing import Optional


class VehicleInterestCreate(BaseModel):

    vehicle_id: int

    search_score: Optional[int] = 0

    review_score: Optional[int] = 0

    faq_score: Optional[int] = 0

    trend_score: Optional[int] = 0

    overall_score: Optional[int] = 0

    ranking: Optional[int] = None



class VehicleInterestResponse(BaseModel):

    id: int

    vehicle_id: int

    search_score: int

    review_score: int

    faq_score: int

    trend_score: int

    overall_score: int

    ranking: Optional[int]


    class Config:
        from_attributes = True