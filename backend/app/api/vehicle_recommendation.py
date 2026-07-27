from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_recommendation import VehicleRecommendation

from app.schemas.vehicle_recommendation import (
    VehicleRecommendationCreate,
    VehicleRecommendationResponse
)


router = APIRouter(
    prefix="/vehicle-recommendations",
    tags=["Vehicle Recommendations"]
)



@router.get(
    "/",
    response_model=list[VehicleRecommendationResponse]
)
def get_vehicle_recommendations(
    db: Session = Depends(get_db)
):

    return db.query(VehicleRecommendation).all()



@router.post(
    "/",
    response_model=VehicleRecommendationResponse
)
def create_vehicle_recommendation(
    data: VehicleRecommendationCreate,
    db: Session = Depends(get_db)
):

    recommendation = VehicleRecommendation(
        **data.model_dump()
    )


    db.add(recommendation)

    db.commit()

    db.refresh(recommendation)


    return recommendation