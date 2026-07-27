from pydantic import BaseModel
from datetime import datetime


class VehicleCreate(BaseModel):

    name: str
    slug: str

    brand_id: int
    category_id: int

    model_year: int | None = None
    price: int | None = None

    image: str | None = None

    status: bool = True



# Brand response
class BrandMiniResponse(BaseModel):

    id: int
    name: str

    class Config:
        from_attributes = True



# Category response
class CategoryMiniResponse(BaseModel):

    id: int
    name: str

    class Config:
        from_attributes = True



# Vehicle Spec Response
class VehicleSpecResponse(BaseModel):

    id: int
    key: str
    value: str

    class Config:
        from_attributes = True



class VehicleResponse(BaseModel):

    id: int

    name: str
    slug: str

    brand_id: int
    category_id: int


    # Relationship data
    brand: BrandMiniResponse
    category: CategoryMiniResponse


    # Vehicle Specifications
    specs: list[VehicleSpecResponse] = []


    model_year: int | None
    price: int | None

    image: str | None

    status: bool

    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True