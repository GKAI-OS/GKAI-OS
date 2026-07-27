from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleInterest(Base):

    __tablename__ = "vehicle_interests"


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


    search_score = Column(
        Integer,
        default=0
    )


    review_score = Column(
        Integer,
        default=0
    )


    faq_score = Column(
        Integer,
        default=0
    )


    trend_score = Column(
        Integer,
        default=0
    )


    overall_score = Column(
        Integer,
        default=0
    )


    ranking = Column(
        Integer,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="interest_score"
    )