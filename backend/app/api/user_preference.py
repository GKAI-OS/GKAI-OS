from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user_preference import UserPreference

from app.schemas.user_preference import (
    UserPreferenceCreate,
    UserPreferenceResponse
)



router = APIRouter(
    prefix="/user-preferences",
    tags=["User Preferences"]
)



@router.get(
    "/",
    response_model=list[UserPreferenceResponse]
)
def get_user_preferences(
    db: Session = Depends(get_db)
):

    return db.query(
        UserPreference
    ).all()



@router.post(
    "/",
    response_model=UserPreferenceResponse
)
def create_user_preference(
    data: UserPreferenceCreate,
    db: Session = Depends(get_db)
):

    preference = UserPreference(
        **data.model_dump()
    )


    db.add(preference)

    db.commit()

    db.refresh(preference)


    return preference