from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user_interaction import UserInteraction

from app.schemas.user_interaction import (
    UserInteractionCreate,
    UserInteractionResponse
)



router = APIRouter(
    prefix="/user-interactions",
    tags=["User Interactions"]
)



@router.get(
    "/",
    response_model=list[UserInteractionResponse]
)
def get_user_interactions(
    db: Session = Depends(get_db)
):

    return db.query(
        UserInteraction
    ).all()



@router.post(
    "/",
    response_model=UserInteractionResponse
)
def create_user_interaction(
    data: UserInteractionCreate,
    db: Session = Depends(get_db)
):

    interaction = UserInteraction(
        **data.model_dump()
    )


    db.add(interaction)

    db.commit()

    db.refresh(interaction)


    return interaction