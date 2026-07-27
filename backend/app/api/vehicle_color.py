from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_color import VehicleColor

from app.schemas.vehicle_color import (
    VehicleColorCreate,
    VehicleColorResponse
)


router = APIRouter(
    prefix="/vehicle-colors",
    tags=["Vehicle Colors"]
)


@router.get(
    "/",
    response_model=list[VehicleColorResponse]
)
def get_vehicle_colors(
    db: Session = Depends(get_db)
):

    return db.query(
        VehicleColor
    ).all()



@router.post(
    "/",
    response_model=VehicleColorResponse
)
def create_vehicle_color(
    data: VehicleColorCreate,
    db: Session = Depends(get_db)
):

    color = VehicleColor(
        **data.model_dump()
    )

    db.add(color)

    db.commit()

    db.refresh(color)

    return color