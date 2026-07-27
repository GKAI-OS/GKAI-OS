from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class VehicleTrend(Base):

    __tablename__ = "vehicle_trends"


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


    trend_keyword = Column(
        String,
        nullable=False
    )


    language = Column(
        String,
        nullable=False
    )


    search_volume = Column(
        Integer,
        default=0
    )


    trend_score = Column(
        Integer,
        default=0
    )


    growth_percentage = Column(
        Float,
        default=0
    )


    trend_direction = Column(
        String,
        nullable=True
    )


    source = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    vehicle = relationship(
        "Vehicle",
        foreign_keys=[vehicle_id]
    )