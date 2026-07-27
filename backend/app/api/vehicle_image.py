from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.vehicle_image import VehicleImage
from app.schemas.vehicle_image import (
    VehicleImageCreate,
    VehicleImageResponse
)


router = APIRouter(
    prefix="/vehicle-images",
    tags=["Vehicle Images"]
)



# Get All Images
@router.get("/", response_model=list[VehicleImageResponse])
def get_vehicle_images(
    db: Session = Depends(get_db)
):

    return db.query(VehicleImage).all()



# Create Image
@router.post("/", response_model=VehicleImageResponse)
def create_vehicle_image(
    image: VehicleImageCreate,
    db: Session = Depends(get_db)
):

    new_image = VehicleImage(
        vehicle_id=image.vehicle_id,
        image=image.image
    )

    db.add(new_image)
    db.commit()
    db.refresh(new_image)

    return new_image



# Get Single Image
@router.get("/{image_id}", response_model=VehicleImageResponse)
def get_vehicle_image(
    image_id: int,
    db: Session = Depends(get_db)
):

    image = db.query(VehicleImage).filter(
        VehicleImage.id == image_id
    ).first()


    if not image:
        raise HTTPException(
            status_code=404,
            detail="Vehicle image not found"
        )


    return image



# Update Image
@router.put("/{image_id}", response_model=VehicleImageResponse)
def update_vehicle_image(
    image_id: int,
    image_data: VehicleImageCreate,
    db: Session = Depends(get_db)
):

    image = db.query(VehicleImage).filter(
        VehicleImage.id == image_id
    ).first()


    if not image:
        raise HTTPException(
            status_code=404,
            detail="Vehicle image not found"
        )


    image.vehicle_id = image_data.vehicle_id
    image.image = image_data.image


    db.commit()
    db.refresh(image)

    return image



# Delete Image
@router.delete("/{image_id}")
def delete_vehicle_image(
    image_id: int,
    db: Session = Depends(get_db)
):

    image = db.query(VehicleImage).filter(
        VehicleImage.id == image_id
    ).first()


    if not image:
        raise HTTPException(
            status_code=404,
            detail="Vehicle image not found"
        )


    db.delete(image)
    db.commit()


    return {
        "message": "Vehicle image deleted successfully"
    }