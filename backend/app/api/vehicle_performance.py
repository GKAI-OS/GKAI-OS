from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_performance import VehiclePerformance

from app.schemas.vehicle_performance import (
    VehiclePerformanceCreate,
    VehiclePerformanceResponse
)


router = APIRouter(
    prefix="/vehicle-performance",
    tags=["Vehicle Performance"]
)



# GET ALL PERFORMANCE
@router.get("/", response_model=list[VehiclePerformanceResponse])
def get_vehicle_performance(
    db: Session = Depends(get_db)
):

    return db.query(VehiclePerformance).all()



# CREATE PERFORMANCE
@router.post("/", response_model=VehiclePerformanceResponse)
def create_vehicle_performance(
    performance: VehiclePerformanceCreate,
    db: Session = Depends(get_db)
):

    new_performance = VehiclePerformance(

        vehicle_id=performance.vehicle_id,

        engine_power=performance.engine_power,

        torque=performance.torque,

        mileage=performance.mileage,

        top_speed=performance.top_speed,

        acceleration=performance.acceleration,

        battery_range=performance.battery_range,

        charging_time=performance.charging_time
    )


    db.add(new_performance)
    db.commit()
    db.refresh(new_performance)


    return new_performance




# GET SINGLE PERFORMANCE
@router.get("/{performance_id}", response_model=VehiclePerformanceResponse)
def get_single_vehicle_performance(
    performance_id: int,
    db: Session = Depends(get_db)
):

    performance = db.query(VehiclePerformance).filter(
        VehiclePerformance.id == performance_id
    ).first()


    if not performance:

        raise HTTPException(
            status_code=404,
            detail="Vehicle performance not found"
        )


    return performance




# UPDATE PERFORMANCE
@router.put("/{performance_id}", response_model=VehiclePerformanceResponse)
def update_vehicle_performance(
    performance_id: int,
    performance_data: VehiclePerformanceCreate,
    db: Session = Depends(get_db)
):

    performance = db.query(VehiclePerformance).filter(
        VehiclePerformance.id == performance_id
    ).first()


    if not performance:

        raise HTTPException(
            status_code=404,
            detail="Vehicle performance not found"
        )


    performance.vehicle_id = performance_data.vehicle_id

    performance.engine_power = performance_data.engine_power

    performance.torque = performance_data.torque

    performance.mileage = performance_data.mileage

    performance.top_speed = performance_data.top_speed

    performance.acceleration = performance_data.acceleration

    performance.battery_range = performance_data.battery_range

    performance.charging_time = performance_data.charging_time


    db.commit()
    db.refresh(performance)


    return performance




# DELETE PERFORMANCE
@router.delete("/{performance_id}")
def delete_vehicle_performance(
    performance_id: int,
    db: Session = Depends(get_db)
):

    performance = db.query(VehiclePerformance).filter(
        VehiclePerformance.id == performance_id
    ).first()


    if not performance:

        raise HTTPException(
            status_code=404,
            detail="Vehicle performance not found"
        )


    db.delete(performance)

    db.commit()


    return {
        "message": "Vehicle performance deleted successfully"
    }