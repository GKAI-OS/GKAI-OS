from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class AIRecommendationCreate(BaseModel):

    vehicle_id: int

    user_query: str

    user_language: Optional[str] = None

    user_budget: Optional[str] = None

    user_need: Optional[str] = None

    matched_intent: Optional[str] = None

    ai_score: int = 0

    confidence_score: int = 0

    recommendation_reason: Optional[str] = None

    ranking: Optional[int] = None



class AIRecommendationResponse(BaseModel):

    id: int

    vehicle_id: int

    user_query: str

    user_language: Optional[str]

    user_budget: Optional[str]

    user_need: Optional[str]

    matched_intent: Optional[str]

    ai_score: int

    confidence_score: int

    recommendation_reason: Optional[str]

    ranking: Optional[int]

    created_at: datetime


    class Config:
        from_attributes = True