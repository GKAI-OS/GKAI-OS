from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.ai_vehicle_score import AIVehicleScore

from app.schemas.ai_vehicle_score import (
    AIVehicleScoreCreate,
    AIVehicleScoreResponse
)


router = APIRouter(
    prefix="/ai-vehicle-scores",
    tags=["AI Vehicle Scores"]
)



@router.get(
    "/",
    response_model=list[AIVehicleScoreResponse]
)
def get_ai_vehicle_scores(
    db: Session = Depends(get_db)
):

    return db.query(
        AIVehicleScore
    ).all()



@router.post(
    "/",
    response_model=AIVehicleScoreResponse
)
def create_ai_vehicle_score(
    data: AIVehicleScoreCreate,
    db: Session = Depends(get_db)
):

    score = AIVehicleScore(
        **data.model_dump()
    )


    db.add(score)

    db.commit()

    db.refresh(score)


    return score