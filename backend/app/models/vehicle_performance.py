from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehiclePerformance(Base):

    __tablename__ = "vehicle_performances"


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


    engine_power = Column(
        String,
        nullable=True
    )


    torque = Column(
        String,
        nullable=True
    )


    mileage = Column(
        String,
        nullable=True
    )


    top_speed = Column(
        String,
        nullable=True
    )


    acceleration = Column(
        String,
        nullable=True
    )


    battery_range = Column(
        String,
        nullable=True
    )


    charging_time = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="performance"
    )