from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.brand import Brand
from app.schemas.brand import BrandResponse


router = APIRouter(
    prefix="/brands",
    tags=["Brands"]
)


@router.get("/", response_model=list[BrandResponse])
def get_brands(db: Session = Depends(get_db)):

    brands = db.query(Brand).all()

    return brands