from pydantic import BaseModel
from typing import Optional


class SearchIntentCreate(BaseModel):

    vehicle_id: int

    query: str

    language: str

    intent_type: str

    search_count: Optional[int] = 0

    trend_score: Optional[int] = 0

    source: Optional[str] = None



class SearchIntentResponse(BaseModel):

    id: int

    vehicle_id: int

    query: str

    language: str

    intent_type: str

    search_count: int

    trend_score: int

    source: Optional[str]


    class Config:
        from_attributes = True