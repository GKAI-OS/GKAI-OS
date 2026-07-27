from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class VehicleReview(Base):

    __tablename__ = "vehicle_reviews"


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


    reviewer_name = Column(
        String,
        nullable=True
    )


    review_type = Column(
        String,
        nullable=True
    )


    rating = Column(
        String,
        nullable=True
    )


    title = Column(
        String,
        nullable=True
    )


    review_text = Column(
        Text,
        nullable=True
    )


    pros = Column(
        Text,
        nullable=True
    )


    cons = Column(
        Text,
        nullable=True
    )


    ownership_experience = Column(
        Text,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        back_populates="reviews"
    )