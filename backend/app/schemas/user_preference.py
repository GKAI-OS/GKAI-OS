from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class UserPreferenceCreate(BaseModel):

    user_id: int

    preferred_brand: Optional[str] = None

    preferred_category: Optional[str] = None

    budget_range: Optional[str] = None

    fuel_preference: Optional[str] = None

    transmission_preference: Optional[str] = None

    usage_type: Optional[str] = None

    language: Optional[str] = None

    city: Optional[str] = None

    preference_score: int = 0



class UserPreferenceResponse(BaseModel):

    id: int

    user_id: int

    preferred_brand: Optional[str]

    preferred_category: Optional[str]

    budget_range: Optional[str]

    fuel_preference: Optional[str]

    transmission_preference: Optional[str]

    usage_type: Optional[str]

    language: Optional[str]

    city: Optional[str]

    preference_score: int

    created_at: datetime

    updated_at: datetime


    class Config:
        from_attributes = True