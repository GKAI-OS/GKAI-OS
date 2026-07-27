from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


# GET ALL CATEGORIES
@router.get("/", response_model=list[CategoryResponse])
def get_categories(
    db: Session = Depends(get_db)
):
    categories = db.query(Category).all()
    return categories



# CREATE CATEGORY
@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):

    existing_category = db.query(Category).filter(
        Category.slug == category.slug
    ).first()

    if existing_category:
        raise HTTPException(
            status_code=400,
            detail="Category slug already exists"
        )


    new_category = Category(
        name=category.name,
        slug=category.slug,
        status=category.status
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category



# UPDATE CATEGORY
@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category_data: CategoryCreate,
    db: Session = Depends(get_db)
):

    category = db.query(Category).filter(
        Category.id == category_id
    ).first()


    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )


    category.name = category_data.name
    category.slug = category_data.slug
    category.status = category_data.status


    db.commit()
    db.refresh(category)

    return category



# DELETE CATEGORY
@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):

    category = db.query(Category).filter(
        Category.id == category_id
    ).first()


    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )


    db.delete(category)
    db.commit()


    return {
        "message": "Category deleted successfully"
    }