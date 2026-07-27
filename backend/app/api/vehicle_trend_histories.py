from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_trend_history import VehicleTrendHistory

from app.schemas.vehicle_trend_history import (
    VehicleTrendHistoryCreate,
    VehicleTrendHistoryResponse
)



router = APIRouter(
    prefix="/vehicle-trend-histories",
    tags=["Vehicle Trend Histories"]
)



@router.get(
    "/",
    response_model=list[VehicleTrendHistoryResponse]
)
def get_vehicle_trend_histories(
    db: Session = Depends(get_db)
):

    return db.query(
        VehicleTrendHistory
    ).all()



@router.post(
    "/",
    response_model=VehicleTrendHistoryResponse
)
def create_vehicle_trend_history(
    data: VehicleTrendHistoryCreate,
    db: Session = Depends(get_db)
):

    history = VehicleTrendHistory(
        **data.model_dump()
    )


    db.add(history)

    db.commit()

    db.refresh(history)


    return history