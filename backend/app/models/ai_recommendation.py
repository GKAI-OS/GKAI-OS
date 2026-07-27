from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class AIRecommendation(Base):

    __tablename__ = "ai_recommendations"


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


    user_query = Column(
        String,
        nullable=False
    )


    user_language = Column(
        String,
        nullable=True
    )


    user_budget = Column(
        String,
        nullable=True
    )


    user_need = Column(
        String,
        nullable=True
    )


    matched_intent = Column(
        String,
        nullable=True
    )


    ai_score = Column(
        Integer,
        default=0
    )


    confidence_score = Column(
        Integer,
        default=0
    )


    recommendation_reason = Column(
        String,
        nullable=True
    )


    ranking = Column(
        Integer,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    vehicle = relationship(
        "Vehicle"
    )