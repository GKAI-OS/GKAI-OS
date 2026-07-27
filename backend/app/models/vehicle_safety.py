from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleSafety(Base):

    __tablename__ = "vehicle_safety"


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


    airbags = Column(
        String,
        nullable=True
    )


    abs = Column(
        Boolean,
        default=False
    )


    ebd = Column(
        Boolean,
        default=False
    )


    traction_control = Column(
        Boolean,
        default=False
    )


    hill_assist = Column(
        Boolean,
        default=False
    )


    esp = Column(
        Boolean,
        default=False
    )


    adas = Column(
        String,
        nullable=True
    )


    safety_rating = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="safety_details"
    )