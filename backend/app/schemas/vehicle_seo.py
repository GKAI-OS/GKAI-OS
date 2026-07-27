from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class VehicleSEOCreate(BaseModel):

    vehicle_id: int

    meta_title: str

    meta_description: str

    seo_slug: str

    primary_keyword: Optional[str] = None

    secondary_keywords: Optional[str] = None

    search_intent: Optional[str] = None

    schema_type: Optional[str] = "Vehicle"

    faq_schema: Optional[str] = None

    review_schema: Optional[str] = None



class VehicleSEOResponse(BaseModel):

    id: int

    vehicle_id: int

    meta_title: str

    meta_description: str

    seo_slug: str

    primary_keyword: Optional[str]

    secondary_keywords: Optional[str]

    search_intent: Optional[str]

    schema_type: Optional[str]

    faq_schema: Optional[str]

    review_schema: Optional[str]

    last_updated: datetime


    class Config:
        from_attributes = True