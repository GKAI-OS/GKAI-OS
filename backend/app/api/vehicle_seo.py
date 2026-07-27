from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_seo import VehicleSEO

from app.schemas.vehicle_seo import (
    VehicleSEOCreate,
    VehicleSEOResponse
)



router = APIRouter(
    prefix="/vehicle-seos",
    tags=["Vehicle SEO"]
)



@router.get(
    "/",
    response_model=list[VehicleSEOResponse]
)
def get_vehicle_seos(
    db: Session = Depends(get_db)
):

    return db.query(VehicleSEO).all()



@router.post(
    "/",
    response_model=VehicleSEOResponse
)
def create_vehicle_seo(
    data: VehicleSEOCreate,
    db: Session = Depends(get_db)
):

    seo = VehicleSEO(
        **data.model_dump()
    )


    db.add(seo)

    db.commit()

    db.refresh(seo)


    return seo