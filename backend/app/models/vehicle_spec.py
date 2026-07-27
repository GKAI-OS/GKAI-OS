from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleSpec(Base):

    __tablename__ = "vehicle_specs"


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


    key = Column(
        String,
        nullable=False
    )


    value = Column(
        String,
        nullable=False
    )


    vehicle = relationship(
        "Vehicle",
        back_populates="specs"
    )