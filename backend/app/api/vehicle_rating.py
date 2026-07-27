from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_rating import VehicleRating

from app.schemas.vehicle_rating import (
    VehicleRatingCreate,
    VehicleRatingResponse
)



router = APIRouter(
    prefix="/vehicle-ratings",
    tags=["Vehicle Ratings"]
)



@router.get(
    "/",
    response_model=list[VehicleRatingResponse]
)
def get_vehicle_ratings(
    db: Session = Depends(get_db)
):

    return db.query(VehicleRating).all()



@router.post(
    "/",
    response_model=VehicleRatingResponse
)
def create_vehicle_rating(
    data: VehicleRatingCreate,
    db: Session = Depends(get_db)
):

    rating = VehicleRating(
        **data.model_dump()
    )


    db.add(rating)

    db.commit()

    db.refresh(rating)


    return rating