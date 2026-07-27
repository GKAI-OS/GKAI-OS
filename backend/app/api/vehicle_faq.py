from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.vehicle_faq import VehicleFAQ
from app.schemas.vehicle_faq import (
    VehicleFAQCreate,
    VehicleFAQResponse
)


router = APIRouter(
    prefix="/vehicle-faqs",
    tags=["Vehicle FAQs"]
)



@router.get(
    "/",
    response_model=list[VehicleFAQResponse]
)
def get_vehicle_faqs(
    db: Session = Depends(get_db)
):

    return db.query(VehicleFAQ).all()



@router.post(
    "/",
    response_model=VehicleFAQResponse
)
def create_vehicle_faq(
    faq: VehicleFAQCreate,
    db: Session = Depends(get_db)
):

    db_faq = VehicleFAQ(

        vehicle_id=faq.vehicle_id,

        question_en=faq.question_en,

        answer_en=faq.answer_en,

        question_hi=faq.question_hi,

        answer_hi=faq.answer_hi,

        faq_type=faq.faq_type
    )


    db.add(db_faq)

    db.commit()

    db.refresh(db_faq)


    return db_faq