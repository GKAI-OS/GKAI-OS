from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_interest import VehicleInterest

from app.schemas.vehicle_interest import (
    VehicleInterestCreate,
    VehicleInterestResponse
)


router = APIRouter(
    prefix="/vehicle-interests",
    tags=["Vehicle Interests"]
)



@router.get(
    "/",
    response_model=list[VehicleInterestResponse]
)
def get_vehicle_interests(
    db: Session = Depends(get_db)
):

    return db.query(VehicleInterest).all()



@router.post(
    "/",
    response_model=VehicleInterestResponse
)
def create_vehicle_interest(
    data: VehicleInterestCreate,
    db: Session = Depends(get_db)
):

    interest = VehicleInterest(
        **data.model_dump()
    )


    db.add(interest)

    db.commit()

    db.refresh(interest)


    return interest