from pydantic import BaseModel
from datetime import datetime


class CategoryCreate(BaseModel):

    name: str
    slug: str
    status: bool = True



class CategoryResponse(BaseModel):

    id: int
    name: str
    slug: str
    status: bool
    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True