from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.vehicle_spec import VehicleSpec
from app.schemas.vehicle_spec import (
    VehicleSpecCreate,
    VehicleSpecResponse
)


router = APIRouter(
    prefix="/vehicle-specs",
    tags=["Vehicle Specs"]
)



@router.get("/", response_model=list[VehicleSpecResponse])
def get_vehicle_specs(
    db: Session = Depends(get_db)
):

    return db.query(VehicleSpec).all()



@router.post("/", response_model=VehicleSpecResponse)
def create_vehicle_spec(
    spec: VehicleSpecCreate,
    db: Session = Depends(get_db)
):

    new_spec = VehicleSpec(
        vehicle_id=spec.vehicle_id,
        key=spec.key,
        value=spec.value
    )

    db.add(new_spec)
    db.commit()
    db.refresh(new_spec)

    return new_spec



@router.get("/{spec_id}", response_model=VehicleSpecResponse)
def get_vehicle_spec(
    spec_id: int,
    db: Session = Depends(get_db)
):

    spec = db.query(VehicleSpec).filter(
        VehicleSpec.id == spec_id
    ).first()


    if not spec:
        raise HTTPException(
            status_code=404,
            detail="Vehicle spec not found"
        )


    return spec



@router.put("/{spec_id}", response_model=VehicleSpecResponse)
def update_vehicle_spec(
    spec_id: int,
    spec_data: VehicleSpecCreate,
    db: Session = Depends(get_db)
):

    spec = db.query(VehicleSpec).filter(
        VehicleSpec.id == spec_id
    ).first()


    if not spec:
        raise HTTPException(
            status_code=404,
            detail="Vehicle spec not found"
        )


    spec.vehicle_id = spec_data.vehicle_id
    spec.key = spec_data.key
    spec.value = spec_data.value


    db.commit()
    db.refresh(spec)

    return spec



@router.delete("/{spec_id}")
def delete_vehicle_spec(
    spec_id: int,
    db: Session = Depends(get_db)
):

    spec = db.query(VehicleSpec).filter(
        VehicleSpec.id == spec_id
    ).first()


    if not spec:
        raise HTTPException(
            status_code=404,
            detail="Vehicle spec not found"
        )


    db.delete(spec)
    db.commit()


    return {
        "message": "Vehicle spec deleted successfully"
    }