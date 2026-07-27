from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class AIVehicleScoreCreate(BaseModel):

    vehicle_id: int

    search_score: int = 0

    review_score: int = 0

    faq_score: int = 0

    trend_score: int = 0

    seo_score: int = 0

    eat_score: int = 0

    overall_score: int = 0

    ranking: Optional[int] = None

    score_reason: Optional[str] = None



class AIVehicleScoreResponse(BaseModel):

    id: int

    vehicle_id: int

    search_score: int

    review_score: int

    faq_score: int

    trend_score: int

    seo_score: int

    eat_score: int

    overall_score: int

    ranking: Optional[int]

    score_reason: Optional[str]

    created_at: datetime


    class Config:
        from_attributes = True