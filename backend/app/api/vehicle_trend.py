from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_trend import VehicleTrend

from app.schemas.vehicle_trend import (
    VehicleTrendCreate,
    VehicleTrendResponse
)



router = APIRouter(
    prefix="/vehicle-trends",
    tags=["Vehicle Trends"]
)



@router.get(
    "/",
    response_model=list[VehicleTrendResponse]
)
def get_vehicle_trends(
    db: Session = Depends(get_db)
):

    return db.query(VehicleTrend).all()




@router.post(
    "/",
    response_model=VehicleTrendResponse
)
def create_vehicle_trend(
    data: VehicleTrendCreate,
    db: Session = Depends(get_db)
):

    trend = VehicleTrend(
        **data.model_dump()
    )


    db.add(trend)

    db.commit()

    db.refresh(trend)


    return trend