from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_fuel import VehicleFuel

from app.schemas.vehicle_fuel import (
    VehicleFuelCreate,
    VehicleFuelResponse
)


router = APIRouter(
    prefix="/vehicle-fuels",
    tags=["Vehicle Fuels"]
)



# GET ALL

@router.get(
    "/",
    response_model=list[VehicleFuelResponse]
)
def get_vehicle_fuels(
    db: Session = Depends(get_db)
):

    return db.query(VehicleFuel).all()



# CREATE

@router.post(
    "/",
    response_model=VehicleFuelResponse
)
def create_vehicle_fuel(
    fuel: VehicleFuelCreate,
    db: Session = Depends(get_db)
):

    new_fuel = VehicleFuel(

        vehicle_id=fuel.vehicle_id,

        fuel_type=fuel.fuel_type,

        fuel_capacity=fuel.fuel_capacity,

        ethanol_percentage=fuel.ethanol_percentage,

        battery_capacity=fuel.battery_capacity,

        range=fuel.range,

        charging_type=fuel.charging_type,

        charging_time=fuel.charging_time
    )


    db.add(new_fuel)

    db.commit()

    db.refresh(new_fuel)


    return new_fuel




# GET SINGLE

@router.get(
    "/{fuel_id}",
    response_model=VehicleFuelResponse
)
def get_vehicle_fuel(
    fuel_id: int,
    db: Session = Depends(get_db)
):

    fuel = db.query(VehicleFuel).filter(
        VehicleFuel.id == fuel_id
    ).first()


    if not fuel:
        raise HTTPException(
            status_code=404,
            detail="Vehicle fuel not found"
        )


    return fuel




# UPDATE

@router.put(
    "/{fuel_id}",
    response_model=VehicleFuelResponse
)
def update_vehicle_fuel(
    fuel_id: int,
    fuel_data: VehicleFuelCreate,
    db: Session = Depends(get_db)
):

    fuel = db.query(VehicleFuel).filter(
        VehicleFuel.id == fuel_id
    ).first()


    if not fuel:
        raise HTTPException(
            status_code=404,
            detail="Vehicle fuel not found"
        )


    fuel.vehicle_id = fuel_data.vehicle_id

    fuel.fuel_type = fuel_data.fuel_type

    fuel.fuel_capacity = fuel_data.fuel_capacity

    fuel.ethanol_percentage = fuel_data.ethanol_percentage

    fuel.battery_capacity = fuel_data.battery_capacity

    fuel.range = fuel_data.range

    fuel.charging_type = fuel_data.charging_type

    fuel.charging_time = fuel_data.charging_time



    db.commit()

    db.refresh(fuel)


    return fuel




# DELETE

@router.delete(
    "/{fuel_id}"
)
def delete_vehicle_fuel(
    fuel_id: int,
    db: Session = Depends(get_db)
):

    fuel = db.query(VehicleFuel).filter(
        VehicleFuel.id == fuel_id
    ).first()


    if not fuel:
        raise HTTPException(
            status_code=404,
            detail="Vehicle fuel not found"
        )


    db.delete(fuel)

    db.commit()


    return {
        "message": "Vehicle fuel deleted successfully"
    }