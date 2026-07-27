from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

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



# =====================
# Get All AI Scores
# =====================

@router.get(
    "/",
    response_model=list[AIVehicleScoreResponse]
)
def get_ai_vehicle_scores(
    db: Session = Depends(get_db)
):

    scores = (
        db.query(AIVehicleScore)
        .all()
    )

    return scores




# =====================
# Get Single AI Score
# =====================

@router.get(
    "/{score_id}",
    response_model=AIVehicleScoreResponse
)
def get_ai_vehicle_score(
    score_id: int,
    db: Session = Depends(get_db)
):

    score = (
        db.query(AIVehicleScore)
        .filter(
            AIVehicleScore.id == score_id
        )
        .first()
    )


    if not score:

        raise HTTPException(
            status_code=404,
            detail="AI Vehicle Score not found"
        )


    return score




# =====================
# Create AI Score
# =====================

@router.post(
    "/",
    response_model=AIVehicleScoreResponse
)
def create_ai_vehicle_score(
    data: AIVehicleScoreCreate,
    db: Session = Depends(get_db)
):


    existing = (
        db.query(AIVehicleScore)
        .filter(
            AIVehicleScore.vehicle_id == data.vehicle_id
        )
        .first()
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="AI score already exists for this vehicle"
        )



    score = AIVehicleScore(
        **data.model_dump()
    )


    db.add(score)

    db.commit()

    db.refresh(score)


    return score




# =====================
# Delete AI Score
# =====================

@router.delete(
    "/{score_id}"
)
def delete_ai_vehicle_score(
    score_id: int,
    db: Session = Depends(get_db)
):

    score = (
        db.query(AIVehicleScore)
        .filter(
            AIVehicleScore.id == score_id
        )
        .first()
    )


    if not score:

        raise HTTPException(
            status_code=404,
            detail="AI Vehicle Score not found"
        )


    db.delete(score)

    db.commit()


    return {
        "message": "AI Vehicle Score deleted successfully"
    }