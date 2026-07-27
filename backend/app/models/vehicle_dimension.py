from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleDimension(Base):

    __tablename__ = "vehicle_dimensions"

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

    length = Column(
        String,
        nullable=True
    )

    width = Column(
        String,
        nullable=True
    )

    height = Column(
        String,
        nullable=True
    )

    wheelbase = Column(
        String,
        nullable=True
    )

    ground_clearance = Column(
        String,
        nullable=True
    )

    boot_space = Column(
        String,
        nullable=True
    )

    kerb_weight = Column(
        String,
        nullable=True
    )

    seating_capacity = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="dimensions"
    )