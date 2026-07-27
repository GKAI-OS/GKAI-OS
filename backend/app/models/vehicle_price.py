from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehiclePrice(Base):

    __tablename__ = "vehicle_prices"


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


    ex_showroom_price = Column(
        Integer,
        nullable=True
    )


    on_road_price = Column(
        Integer,
        nullable=True
    )


    insurance = Column(
        Integer,
        nullable=True
    )


    registration_charge = Column(
        Integer,
        nullable=True
    )


    discount = Column(
        Integer,
        nullable=True
    )


    emi = Column(
        Integer,
        nullable=True
    )


    notes = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="prices"
    )