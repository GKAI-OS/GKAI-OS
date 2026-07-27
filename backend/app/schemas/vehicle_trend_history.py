from pydantic import BaseModel
from typing import Optional
from datetime import date



class VehicleTrendHistoryCreate(BaseModel):

    vehicle_id: int

    trend_id: Optional[int] = None

    record_date: Optional[date] = None

    search_volume: int

    trend_score: int

    growth_percentage: Optional[int] = None



class VehicleTrendHistoryResponse(BaseModel):

    id: int

    vehicle_id: int

    trend_id: Optional[int]

    record_date: date

    search_volume: int

    trend_score: int

    growth_percentage: Optional[int]


    class Config:
        from_attributes = True