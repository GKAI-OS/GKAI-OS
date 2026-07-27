from pydantic import BaseModel
from typing import Optional



class VehicleReviewCreate(BaseModel):

    vehicle_id: int

    reviewer_name: Optional[str] = None

    review_type: Optional[str] = None

    rating: Optional[str] = None

    title: Optional[str] = None

    review_text: Optional[str] = None

    pros: Optional[str] = None

    cons: Optional[str] = None

    ownership_experience: Optional[str] = None



class VehicleReviewResponse(BaseModel):

    id: int

    vehicle_id: int

    reviewer_name: Optional[str]

    review_type: Optional[str]

    rating: Optional[str]

    title: Optional[str]

    review_text: Optional[str]

    pros: Optional[str]

    cons: Optional[str]

    ownership_experience: Optional[str]


    class Config:
        from_attributes = True