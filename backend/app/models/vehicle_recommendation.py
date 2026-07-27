from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleRecommendation(Base):

    __tablename__ = "vehicle_recommendations"


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


    user_need = Column(
        String,
        nullable=False
    )


    budget_range = Column(
        String,
        nullable=True
    )


    recommendation_score = Column(
        Integer,
        default=0
    )


    reason = Column(
        String,
        nullable=True
    )


    priority = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="recommendations"
    )