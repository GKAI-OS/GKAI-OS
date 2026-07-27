from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.brand import Brand
from app.schemas.brand import BrandCreate, BrandResponse


router = APIRouter(
    prefix="/brands",
    tags=["Brands"]
)


# GET ALL BRANDS
@router.get("/", response_model=list[BrandResponse])
def get_brands(
    db: Session = Depends(get_db)
):
    brands = db.query(Brand).all()
    return brands


# CREATE BRAND
@router.post("/", response_model=BrandResponse)
def create_brand(
    brand: BrandCreate,
    db: Session = Depends(get_db)
):

    existing_brand = db.query(Brand).filter(
        Brand.slug == brand.slug
    ).first()

    if existing_brand:
        raise HTTPException(
            status_code=400,
            detail="Brand slug already exists"
        )

    new_brand = Brand(
        name=brand.name,
        slug=brand.slug,
        logo=brand.logo,
        country=brand.country,
        status=brand.status
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand


# UPDATE BRAND
@router.put("/{brand_id}", response_model=BrandResponse)
def update_brand(
    brand_id: int,
    brand_data: BrandCreate,
    db: Session = Depends(get_db)
):

    brand = db.query(Brand).filter(
        Brand.id == brand_id
    ).first()

    if not brand:
        raise HTTPException(
            status_code=404,
            detail="Brand not found"
        )

    brand.name = brand_data.name
    brand.slug = brand_data.slug
    brand.logo = brand_data.logo
    brand.country = brand_data.country
    brand.status = brand_data.status

    db.commit()
    db.refresh(brand)

    return brand


# DELETE BRAND
@router.delete("/{brand_id}")
def delete_brand(
    brand_id: int,
    db: Session = Depends(get_db)
):

    brand = db.query(Brand).filter(
        Brand.id == brand_id
    ).first()

    if not brand:
        raise HTTPException(
            status_code=404,
            detail="Brand not found"
        )

    db.delete(brand)
    db.commit()

    return {
        "message": "Brand deleted successfully"
    }