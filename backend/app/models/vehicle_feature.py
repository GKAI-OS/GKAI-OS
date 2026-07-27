from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleFeature(Base):

    __tablename__ = "vehicle_features"


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


    feature = Column(
        String,
        nullable=False
    )


    vehicle = relationship(
        "Vehicle",
        backref="features"
    )