from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class ModuleNameCreate(BaseModel):

    name: str

    description: Optional[str] = None

    status: Optional[str] = "Active"



class ModuleNameResponse(BaseModel):

    id: int

    name: str

    description: Optional[str]

    status: str

    created_at: datetime

    updated_at: datetime


    class Config:
        from_attributes = True