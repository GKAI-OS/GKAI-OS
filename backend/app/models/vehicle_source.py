from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleSource(Base):

    __tablename__ = "vehicle_sources"


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


    source_name = Column(
        String,
        nullable=False
    )


    source_type = Column(
        String,
        nullable=False
    )


    source_url = Column(
        String,
        nullable=True
    )


    data_category = Column(
        String,
        nullable=False
    )


    verified_status = Column(
        String,
        default="Pending"
    )


    verified_by = Column(
        String,
        nullable=True
    )


    verified_date = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="sources"
    )