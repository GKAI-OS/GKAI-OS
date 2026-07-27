from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.vehicle_feature import VehicleFeature
from app.schemas.vehicle_feature import (
    VehicleFeatureCreate,
    VehicleFeatureResponse
)


router = APIRouter(
    prefix="/vehicle-features",
    tags=["Vehicle Features"]
)


# GET ALL FEATURES
@router.get("/", response_model=list[VehicleFeatureResponse])
def get_vehicle_features(
    db: Session = Depends(get_db)
):

    return db.query(VehicleFeature).all()



# CREATE FEATURE
@router.post("/", response_model=VehicleFeatureResponse)
def create_vehicle_feature(
    feature: VehicleFeatureCreate,
    db: Session = Depends(get_db)
):

    new_feature = VehicleFeature(
        vehicle_id=feature.vehicle_id,
        feature=feature.feature
    )

    db.add(new_feature)
    db.commit()
    db.refresh(new_feature)

    return new_feature



# GET SINGLE FEATURE
@router.get("/{feature_id}", response_model=VehicleFeatureResponse)
def get_vehicle_feature(
    feature_id: int,
    db: Session = Depends(get_db)
):

    feature = db.query(VehicleFeature).filter(
        VehicleFeature.id == feature_id
    ).first()


    if not feature:
        raise HTTPException(
            status_code=404,
            detail="Vehicle feature not found"
        )


    return feature



# UPDATE FEATURE
@router.put("/{feature_id}", response_model=VehicleFeatureResponse)
def update_vehicle_feature(
    feature_id: int,
    feature_data: VehicleFeatureCreate,
    db: Session = Depends(get_db)
):

    feature = db.query(VehicleFeature).filter(
        VehicleFeature.id == feature_id
    ).first()


    if not feature:
        raise HTTPException(
            status_code=404,
            detail="Vehicle feature not found"
        )


    feature.vehicle_id = feature_data.vehicle_id
    feature.feature = feature_data.feature


    db.commit()
    db.refresh(feature)

    return feature



# DELETE FEATURE
@router.delete("/{feature_id}")
def delete_vehicle_feature(
    feature_id: int,
    db: Session = Depends(get_db)
):

    feature = db.query(VehicleFeature).filter(
        VehicleFeature.id == feature_id
    ).first()


    if not feature:
        raise HTTPException(
            status_code=404,
            detail="Vehicle feature not found"
        )


    db.delete(feature)
    db.commit()


    return {
        "message": "Vehicle feature deleted successfully"
    }