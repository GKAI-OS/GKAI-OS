from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_source import VehicleSource

from app.schemas.vehicle_source import (
    VehicleSourceCreate,
    VehicleSourceResponse
)


router = APIRouter(
    prefix="/vehicle-sources",
    tags=["Vehicle Sources"]
)



@router.get(
    "/",
    response_model=list[VehicleSourceResponse]
)
def get_vehicle_sources(
    db: Session = Depends(get_db)
):

    return db.query(VehicleSource).all()



@router.post(
    "/",
    response_model=VehicleSourceResponse
)
def create_vehicle_source(
    data: VehicleSourceCreate,
    db: Session = Depends(get_db)
):

    source = VehicleSource(
        **data.model_dump()
    )

    db.add(source)

    db.commit()

    db.refresh(source)

    return source