from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.vehicle_dimension import VehicleDimension
from app.schemas.vehicle_dimension import (
    VehicleDimensionCreate,
    VehicleDimensionResponse
)


router = APIRouter(
    prefix="/vehicle-dimensions",
    tags=["Vehicle Dimensions"]
)


@router.get(
    "/",
    response_model=list[VehicleDimensionResponse]
)
def get_vehicle_dimensions(
    db: Session = Depends(get_db)
):

    return db.query(
        VehicleDimension
    ).all()



@router.post(
    "/",
    response_model=VehicleDimensionResponse
)
def create_vehicle_dimension(
    data: VehicleDimensionCreate,
    db: Session = Depends(get_db)
):

    dimension = VehicleDimension(
        **data.model_dump()
    )

    db.add(dimension)

    db.commit()

    db.refresh(dimension)

    return dimension