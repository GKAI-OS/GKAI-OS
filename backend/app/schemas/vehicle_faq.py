from pydantic import BaseModel
from typing import Optional


class VehicleFAQCreate(BaseModel):

    vehicle_id: int

    question_en: str

    answer_en: str

    question_hi: Optional[str] = None

    answer_hi: Optional[str] = None

    faq_type: Optional[str] = None



class VehicleFAQResponse(BaseModel):

    id: int

    vehicle_id: int

    question_en: str

    answer_en: str

    question_hi: Optional[str]

    answer_hi: Optional[str]

    faq_type: Optional[str]


    class Config:
        from_attributes = True