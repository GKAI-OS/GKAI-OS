from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class AIVehicleScore(Base):

    __tablename__ = "ai_vehicle_scores"


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


    search_score = Column(
        Integer,
        default=0
    )


    review_score = Column(
        Integer,
        default=0
    )


    faq_score = Column(
        Integer,
        default=0
    )


    trend_score = Column(
        Integer,
        default=0
    )


    seo_score = Column(
        Integer,
        default=0
    )


    eat_score = Column(
        Integer,
        default=0
    )


    overall_score = Column(
        Integer,
        default=0
    )


    ranking = Column(
        Integer,
        nullable=True
    )


    score_reason = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    vehicle = relationship(
        "Vehicle"
    )