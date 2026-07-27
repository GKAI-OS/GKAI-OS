from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    CheckConstraint
)

from datetime import datetime

from app.database import Base


class VehicleRating(Base):

    __tablename__ = "vehicle_ratings"


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


    user_id = Column(
        Integer,
        nullable=True
    )


    rating = Column(
        Integer,
        nullable=False
    )


    title = Column(
        String,
        nullable=True
    )


    review_text = Column(
        String,
        nullable=True
    )


    rating_type = Column(
        String,
        nullable=True
    )


    source = Column(
        String,
        nullable=True
    )


    status = Column(
        String,
        default="Active"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    # Rating only between 1 and 5 stars
    __table_args__ = (
        CheckConstraint(
            "rating >= 1 AND rating <= 5",
            name="check_rating_between_1_and_5"
        ),
    )