from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleMileage(Base):

    __tablename__ = "vehicle_mileage"

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
        nullable=True
    )

    city_mileage = Column(
        String,
        nullable=True
    )

    highway_mileage = Column(
        String,
        nullable=True
    )

    claimed_mileage = Column(
        String,
        nullable=True
    )

    real_world_mileage = Column(
        String,
        nullable=True
    )

    battery_range = Column(
        String,
        nullable=True
    )

    efficiency = Column(
        String,
        nullable=True
    )

    vehicle = relationship(
        "Vehicle",
        backref="mileage_details"
    )