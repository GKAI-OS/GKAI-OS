from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class UserInteractionCreate(BaseModel):

    user_id: Optional[int] = None

    vehicle_id: int

    action_type: str

    search_query: Optional[str] = None

    language: Optional[str] = None

    session_id: Optional[str] = None

    interest_score: int = 0



class UserInteractionResponse(BaseModel):

    id: int

    user_id: Optional[int]

    vehicle_id: int

    action_type: str

    search_query: Optional[str]

    language: Optional[str]

    session_id: Optional[str]

    interest_score: int

    created_at: datetime


    class Config:
        from_attributes = True