from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.vehicle_variant import VehicleVariant

from app.schemas.vehicle_variant import (
    VehicleVariantCreate,
    VehicleVariantResponse
)


router = APIRouter(
    prefix="/vehicle-variants",
    tags=["Vehicle Variants"]
)



# GET ALL VARIANTS
@router.get("/", response_model=list[VehicleVariantResponse])
def get_vehicle_variants(
    db: Session = Depends(get_db)
):

    return db.query(VehicleVariant).all()



# CREATE VARIANT
@router.post("/", response_model=VehicleVariantResponse)
def create_vehicle_variant(
    variant: VehicleVariantCreate,
    db: Session = Depends(get_db)
):

    new_variant = VehicleVariant(
        vehicle_id=variant.vehicle_id,
        variant_name=variant.variant_name,
        engine=variant.engine,
        fuel_type=variant.fuel_type,
        transmission=variant.transmission,
        price=variant.price,
        status=variant.status
    )


    db.add(new_variant)
    db.commit()
    db.refresh(new_variant)


    return new_variant




# GET SINGLE VARIANT
@router.get("/{variant_id}", response_model=VehicleVariantResponse)
def get_vehicle_variant(
    variant_id: int,
    db: Session = Depends(get_db)
):

    variant = db.query(VehicleVariant).filter(
        VehicleVariant.id == variant_id
    ).first()


    if not variant:
        raise HTTPException(
            status_code=404,
            detail="Vehicle variant not found"
        )


    return variant




# UPDATE VARIANT
@router.put("/{variant_id}", response_model=VehicleVariantResponse)
def update_vehicle_variant(
    variant_id: int,
    variant_data: VehicleVariantCreate,
    db: Session = Depends(get_db)
):

    variant = db.query(VehicleVariant).filter(
        VehicleVariant.id == variant_id
    ).first()


    if not variant:
        raise HTTPException(
            status_code=404,
            detail="Vehicle variant not found"
        )


    variant.vehicle_id = variant_data.vehicle_id
    variant.variant_name = variant_data.variant_name
    variant.engine = variant_data.engine
    variant.fuel_type = variant_data.fuel_type
    variant.transmission = variant_data.transmission
    variant.price = variant_data.price
    variant.status = variant_data.status


    db.commit()
    db.refresh(variant)


    return variant




# DELETE VARIANT
@router.delete("/{variant_id}")
def delete_vehicle_variant(
    variant_id: int,
    db: Session = Depends(get_db)
):

    variant = db.query(VehicleVariant).filter(
        VehicleVariant.id == variant_id
    ).first()


    if not variant:
        raise HTTPException(
            status_code=404,
            detail="Vehicle variant not found"
        )


    db.delete(variant)
    db.commit()


    return {
        "message": "Vehicle variant deleted successfully"
    }