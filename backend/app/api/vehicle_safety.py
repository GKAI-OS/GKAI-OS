from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_safety import VehicleSafety

from app.schemas.vehicle_safety import (
    VehicleSafetyCreate,
    VehicleSafetyResponse
)


router = APIRouter(
    prefix="/vehicle-safety",
    tags=["Vehicle Safety"]
)



# GET ALL SAFETY DATA
@router.get(
    "/",
    response_model=list[VehicleSafetyResponse]
)
def get_vehicle_safety(
    db: Session = Depends(get_db)
):

    return db.query(VehicleSafety).all()



# CREATE SAFETY DATA
@router.post(
    "/",
    response_model=VehicleSafetyResponse
)
def create_vehicle_safety(
    safety: VehicleSafetyCreate,
    db: Session = Depends(get_db)
):

    new_safety = VehicleSafety(

        vehicle_id=safety.vehicle_id,

        airbags=safety.airbags,

        abs=safety.abs,

        ebd=safety.ebd,

        traction_control=safety.traction_control,

        hill_assist=safety.hill_assist,

        esp=safety.esp,

        adas=safety.adas,

        safety_rating=safety.safety_rating
    )


    db.add(new_safety)

    db.commit()

    db.refresh(new_safety)


    return new_safety



# GET SINGLE SAFETY
@router.get(
    "/{safety_id}",
    response_model=VehicleSafetyResponse
)
def get_single_vehicle_safety(
    safety_id:int,
    db:Session = Depends(get_db)
):

    safety = db.query(VehicleSafety).filter(
        VehicleSafety.id == safety_id
    ).first()


    if not safety:

        raise HTTPException(
            status_code=404,
            detail="Vehicle safety not found"
        )


    return safety



# UPDATE SAFETY
@router.put(
    "/{safety_id}",
    response_model=VehicleSafetyResponse
)
def update_vehicle_safety(
    safety_id:int,
    safety_data:VehicleSafetyCreate,
    db:Session = Depends(get_db)
):

    safety = db.query(VehicleSafety).filter(
        VehicleSafety.id == safety_id
    ).first()


    if not safety:

        raise HTTPException(
            status_code=404,
            detail="Vehicle safety not found"
        )


    safety.vehicle_id = safety_data.vehicle_id
    safety.airbags = safety_data.airbags
    safety.abs = safety_data.abs
    safety.ebd = safety_data.ebd
    safety.traction_control = safety_data.traction_control
    safety.hill_assist = safety_data.hill_assist
    safety.esp = safety_data.esp
    safety.adas = safety_data.adas
    safety.safety_rating = safety_data.safety_rating


    db.commit()

    db.refresh(safety)


    return safety



# DELETE SAFETY
@router.delete(
    "/{safety_id}"
)
def delete_vehicle_safety(
    safety_id:int,
    db:Session = Depends(get_db)
):

    safety = db.query(VehicleSafety).filter(
        VehicleSafety.id == safety_id
    ).first()


    if not safety:

        raise HTTPException(
            status_code=404,
            detail="Vehicle safety not found"
        )


    db.delete(safety)

    db.commit()


    return {
        "message":"Vehicle safety deleted successfully"
    }