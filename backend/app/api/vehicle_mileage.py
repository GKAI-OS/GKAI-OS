from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_mileage import VehicleMileage
from app.schemas.vehicle_mileage import (
    VehicleMileageCreate,
    VehicleMileageResponse
)


router = APIRouter(
    prefix="/vehicle-mileage",
    tags=["Vehicle Mileage"]
)


@router.get(
    "/",
    response_model=list[VehicleMileageResponse]
)
def get_vehicle_mileage(
    db: Session = Depends(get_db)
):

    return db.query(VehicleMileage).all()



@router.post(
    "/",
    response_model=VehicleMileageResponse
)
def create_vehicle_mileage(
    data: VehicleMileageCreate,
    db: Session = Depends(get_db)
):

    mileage = VehicleMileage(
        **data.dict()
    )

    db.add(mileage)

    db.commit()

    db.refresh(mileage)

    return mileage