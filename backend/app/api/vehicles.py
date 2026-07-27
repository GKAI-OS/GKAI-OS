from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.database import get_db

from app.models.vehicle import Vehicle

from app.schemas.vehicle import (
    VehicleCreate,
    VehicleResponse
)


router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)



# =====================
# Get All Vehicles
# =====================

@router.get("/", response_model=list[VehicleResponse])
def get_vehicles(
    db: Session = Depends(get_db)
):

    vehicles = (
        db.query(Vehicle)
        .options(
            joinedload(Vehicle.brand),
            joinedload(Vehicle.category),
            joinedload(Vehicle.specs),
            joinedload(Vehicle.ratings),
            joinedload(Vehicle.reviews),
            joinedload(Vehicle.prices),
            joinedload(Vehicle.seo)
        )
        .all()
    )

    return vehicles




# =====================
# Get Single Vehicle
# =====================

@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db)
):

    vehicle = (
        db.query(Vehicle)
        .options(
            joinedload(Vehicle.brand),
            joinedload(Vehicle.category),
            joinedload(Vehicle.specs),
            joinedload(Vehicle.ratings),
            joinedload(Vehicle.reviews),
            joinedload(Vehicle.prices),
            joinedload(Vehicle.seo)
        )
        .filter(
            Vehicle.id == vehicle_id
        )
        .first()
    )


    if not vehicle:

        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )


    return vehicle




# =====================
# Create Vehicle
# =====================

@router.post("/", response_model=VehicleResponse)
def create_vehicle(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db)
):

    existing = (
        db.query(Vehicle)
        .filter(
            Vehicle.slug == vehicle.slug
        )
        .first()
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Vehicle slug already exists"
        )


    new_vehicle = Vehicle(

        name=vehicle.name,

        slug=vehicle.slug,

        brand_id=vehicle.brand_id,

        category_id=vehicle.category_id,

        model_year=vehicle.model_year,

        price=vehicle.price,

        image=vehicle.image,

        status=vehicle.status
    )


    db.add(new_vehicle)

    db.commit()

    db.refresh(new_vehicle)


    return new_vehicle




# =====================
# Update Vehicle
# =====================

@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(
    vehicle_id: int,

    vehicle_data: VehicleCreate,

    db: Session = Depends(get_db)
):

    vehicle = (
        db.query(Vehicle)
        .filter(
            Vehicle.id == vehicle_id
        )
        .first()
    )


    if not vehicle:

        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )


    vehicle.name = vehicle_data.name

    vehicle.slug = vehicle_data.slug

    vehicle.brand_id = vehicle_data.brand_id

    vehicle.category_id = vehicle_data.category_id

    vehicle.model_year = vehicle_data.model_year

    vehicle.price = vehicle_data.price

    vehicle.image = vehicle_data.image

    vehicle.status = vehicle_data.status


    db.commit()

    db.refresh(vehicle)


    return vehicle




# =====================
# Delete Vehicle
# =====================

@router.delete("/{vehicle_id}")
def delete_vehicle(
    vehicle_id: int,

    db: Session = Depends(get_db)
):

    vehicle = (
        db.query(Vehicle)
        .filter(
            Vehicle.id == vehicle_id
        )
        .first()
    )


    if not vehicle:

        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )


    db.delete(vehicle)

    db.commit()


    return {
        "message": "Vehicle deleted successfully"
    }