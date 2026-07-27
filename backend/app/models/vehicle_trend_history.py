from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

from app.database import Base


class VehicleTrendHistory(Base):

    __tablename__ = "vehicle_trend_history"


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


    trend_id = Column(
        Integer,
        ForeignKey("vehicle_trends.id"),
        nullable=True
    )


    record_date = Column(
        Date,
        default=date.today
    )


    search_volume = Column(
        Integer,
        nullable=False
    )


    trend_score = Column(
        Integer,
        nullable=False
    )


    growth_percentage = Column(
        Integer,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle"
    )


    trend = relationship(
        "VehicleTrend"
    )