from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleFAQ(Base):

    __tablename__ = "vehicle_faqs"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )


    question_en = Column(
        String,
        nullable=False
    )


    answer_en = Column(
        String,
        nullable=False
    )


    question_hi = Column(
        String,
        nullable=True
    )


    answer_hi = Column(
        String,
        nullable=True
    )


    faq_type = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="faqs"
    )