from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleVariant(Base):

    __tablename__ = "vehicle_variants"


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


    variant_name = Column(
        String,
        nullable=False
    )


    engine = Column(
        String,
        nullable=True
    )


    fuel_type = Column(
        String,
        nullable=True
    )


    transmission = Column(
        String,
        nullable=True
    )


    price = Column(
        Integer,
        nullable=True
    )


    status = Column(
        Boolean,
        default=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="variants"
    )