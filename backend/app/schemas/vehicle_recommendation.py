from pydantic import BaseModel
from typing import Optional


class VehicleRecommendationCreate(BaseModel):

    vehicle_id: int

    user_need: str

    budget_range: Optional[str] = None

    recommendation_score: Optional[int] = 0

    reason: Optional[str] = None

    priority: Optional[str] = None



class VehicleRecommendationResponse(BaseModel):

    id: int

    vehicle_id: int

    user_need: str

    budget_range: Optional[str]

    recommendation_score: int

    reason: Optional[str]

    priority: Optional[str]


    class Config:
        from_attributes = True