from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_comparison import VehicleComparison

from app.schemas.vehicle_comparison import (
    VehicleComparisonCreate,
    VehicleComparisonResponse
)


router = APIRouter(
    prefix="/vehicle-comparisons",
    tags=["Vehicle Comparisons"]
)



@router.get(
    "/",
    response_model=list[VehicleComparisonResponse]
)
def get_vehicle_comparisons(
    db: Session = Depends(get_db)
):

    return db.query(VehicleComparison).all()



@router.post(
    "/",
    response_model=VehicleComparisonResponse
)
def create_vehicle_comparison(
    data: VehicleComparisonCreate,
    db: Session = Depends(get_db)
):

    comparison = VehicleComparison(
        **data.model_dump()
    )


    db.add(comparison)

    db.commit()

    db.refresh(comparison)


    return comparison