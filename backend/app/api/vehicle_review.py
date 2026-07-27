from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_review import VehicleReview

from app.schemas.vehicle_review import (
    VehicleReviewCreate,
    VehicleReviewResponse
)



router = APIRouter(
    prefix="/vehicle-reviews",
    tags=["Vehicle Reviews"]
)



@router.get(
    "/",
    response_model=list[VehicleReviewResponse]
)
def get_vehicle_reviews(
    db: Session = Depends(get_db)
):

    return db.query(VehicleReview).all()



@router.post(
    "/",
    response_model=VehicleReviewResponse
)
def create_vehicle_review(
    review: VehicleReviewCreate,
    db: Session = Depends(get_db)
):

    db_review = VehicleReview(
        **review.dict()
    )

    db.add(db_review)

    db.commit()

    db.refresh(db_review)

    return db_review