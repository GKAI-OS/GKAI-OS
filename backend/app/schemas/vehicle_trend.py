from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class VehicleTrendCreate(BaseModel):

    vehicle_id: int

    trend_keyword: str

    language: str

    search_volume: int = 0

    trend_score: int = 0

    growth_percentage: float = 0

    trend_direction: Optional[str] = None

    source: Optional[str] = None




class VehicleTrendResponse(BaseModel):

    id: int

    vehicle_id: int

    trend_keyword: str

    language: str

    search_volume: int

    trend_score: int

    growth_percentage: float

    trend_direction: Optional[str]

    source: Optional[str]

    created_at: datetime


    class Config:
        from_attributes = True