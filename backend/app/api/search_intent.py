from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.search_intent import SearchIntent

from app.schemas.search_intent import (
    SearchIntentCreate,
    SearchIntentResponse
)


router = APIRouter(
    prefix="/search-intents",
    tags=["Search Intents"]
)



@router.get(
    "/",
    response_model=list[SearchIntentResponse]
)
def get_search_intents(
    db: Session = Depends(get_db)
):

    return db.query(SearchIntent).all()



@router.post(
    "/",
    response_model=SearchIntentResponse
)
def create_search_intent(
    data: SearchIntentCreate,
    db: Session = Depends(get_db)
):

    intent = SearchIntent(
        **data.model_dump()
    )

    db.add(intent)

    db.commit()

    db.refresh(intent)

    return intent