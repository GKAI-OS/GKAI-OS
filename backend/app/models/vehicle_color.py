from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleColor(Base):

    __tablename__ = "vehicle_colors"


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


    color_name = Column(
        String,
        nullable=False
    )


    color_code = Column(
        String,
        nullable=True
    )


    image = Column(
        String,
        nullable=True
    )


    availability = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="colors"
    )