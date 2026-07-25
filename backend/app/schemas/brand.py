from pydantic import BaseModel
from datetime import datetime


class BrandBase(BaseModel):
    name: str
    slug: str
    logo: str | None = None
    country: str | None = None
    status: bool = True


class BrandCreate(BrandBase):
    pass


class BrandResponse(BrandBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True