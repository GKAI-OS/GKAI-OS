from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleFuel(Base):

    __tablename__ = "vehicle_fuels"


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


    fuel_type = Column(
        String,
        nullable=False
    )


    fuel_capacity = Column(
        String,
        nullable=True
    )


    ethanol_percentage = Column(
        String,
        nullable=True
    )


    battery_capacity = Column(
        String,
        nullable=True
    )


    range = Column(
        String,
        nullable=True
    )


    charging_type = Column(
        String,
        nullable=True
    )


    charging_time = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="fuel_details"
    )