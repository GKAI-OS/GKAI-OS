from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.ai_recommendation import AIRecommendation

from app.schemas.ai_recommendation import (
    AIRecommendationCreate,
    AIRecommendationResponse
)



router = APIRouter(
    prefix="/ai-recommendations",
    tags=["AI Recommendations"]
)



@router.get(
    "/",
    response_model=list[AIRecommendationResponse]
)
def get_ai_recommendations(
    db: Session = Depends(get_db)
):

    return db.query(
        AIRecommendation
    ).all()



@router.post(
    "/",
    response_model=AIRecommendationResponse
)
def create_ai_recommendation(
    data: AIRecommendationCreate,
    db: Session = Depends(get_db)
):

    recommendation = AIRecommendation(
        **data.model_dump()
    )


    db.add(recommendation)

    db.commit()

    db.refresh(recommendation)


    return recommendation