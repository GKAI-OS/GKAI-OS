from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleComparison(Base):

    __tablename__ = "vehicle_comparisons"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    vehicle_id_1 = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )


    vehicle_id_2 = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )


    comparison_title = Column(
        String,
        nullable=False
    )


    winner = Column(
        String,
        nullable=True
    )


    reason = Column(
        String,
        nullable=True
    )


    comparison_type = Column(
        String,
        nullable=True
    )


    vehicle_1 = relationship(
        "Vehicle",
        foreign_keys=[vehicle_id_1]
    )


    vehicle_2 = relationship(
        "Vehicle",
        foreign_keys=[vehicle_id_2]
    )