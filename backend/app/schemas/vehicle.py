from pydantic import BaseModel, Field
from datetime import datetime


# =====================
# Vehicle Create
# =====================

class VehicleCreate(BaseModel):

    name: str

    slug: str

    brand_id: int

    category_id: int

    model_year: int | None = None

    price: int | None = None

    image: str | None = None

    status: bool = True



# =====================
# Brand Response
# =====================

class BrandMiniResponse(BaseModel):

    id: int

    name: str


    class Config:
        from_attributes = True



# =====================
# Category Response
# =====================

class CategoryMiniResponse(BaseModel):

    id: int

    name: str


    class Config:
        from_attributes = True



# =====================
# Vehicle Spec Response
# =====================

class VehicleSpecResponse(BaseModel):

    id: int

    key: str

    value: str


    class Config:
        from_attributes = True



# =====================
# Vehicle Rating Response
# =====================

class VehicleRatingResponse(BaseModel):

    id: int

    rating: int

    title: str | None = None

    review_text: str | None = None

    rating_type: str | None = None

    source: str | None = None

    status: str

    created_at: datetime


    class Config:
        from_attributes = True



# =====================
# Vehicle Review Response
# =====================

class VehicleReviewResponse(BaseModel):

    id: int

    reviewer_name: str | None = None

    review_type: str | None = None

    rating: str | None = None

    title: str | None = None

    review_text: str | None = None

    pros: str | None = None

    cons: str | None = None

    ownership_experience: str | None = None


    class Config:
        from_attributes = True



# =====================
# Vehicle Price Response
# =====================

class VehiclePriceResponse(BaseModel):

    id: int

    ex_showroom_price: int | None = None

    on_road_price: int | None = None

    insurance: int | None = None

    registration_charge: int | None = None

    discount: int | None = None

    emi: int | None = None

    notes: str | None = None


    class Config:
        from_attributes = True



# =====================
# Vehicle SEO Response
# =====================

class VehicleSEOResponse(BaseModel):

    id: int

    meta_title: str

    meta_description: str

    seo_slug: str

    primary_keyword: str | None = None

    secondary_keywords: str | None = None

    search_intent: str | None = None

    schema_type: str

    faq_schema: str | None = None

    review_schema: str | None = None

    last_updated: datetime


    class Config:
        from_attributes = True



# =====================
# Vehicle Main Response
# =====================

class VehicleResponse(BaseModel):

    id: int

    name: str

    slug: str


    brand_id: int

    category_id: int


    # =====================
    # Relationships
    # =====================

    brand: BrandMiniResponse

    category: CategoryMiniResponse


    # =====================
    # Specifications
    # =====================

    specs: list[VehicleSpecResponse] = Field(
        default_factory=list
    )


    # =====================
    # Ratings
    # =====================

    ratings: list[VehicleRatingResponse] = Field(
        default_factory=list
    )


    # =====================
    # Reviews
    # =====================

    reviews: list[VehicleReviewResponse] = Field(
        default_factory=list
    )


    # =====================
    # Prices
    # =====================

    prices: list[VehiclePriceResponse] = Field(
        default_factory=list
    )


    # =====================
    # SEO
    # =====================

    seo: list[VehicleSEOResponse] = Field(
        default_factory=list
    )


    model_year: int | None = None

    price: int | None = None

    image: str | None = None

    status: bool


    created_at: datetime

    updated_at: datetime


    class Config:
        from_attributes = True