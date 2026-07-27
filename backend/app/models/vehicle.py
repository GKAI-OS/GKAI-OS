from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Vehicle(Base):

    __tablename__ = "vehicles"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        nullable=False
    )


    slug = Column(
        String,
        unique=True,
        nullable=False
    )


    brand_id = Column(
        Integer,
        ForeignKey("brands.id"),
        nullable=False
    )


    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )


    model_year = Column(
        Integer,
        nullable=True
    )


    price = Column(
        Integer,
        nullable=True
    )


    image = Column(
        String,
        nullable=True
    )


    status = Column(
        Boolean,
        default=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )



    # =====================
    # Relationships
    # =====================


    brand = relationship(
        "Brand",
        backref="vehicles"
    )


    category = relationship(
        "Category",
        backref="vehicles"
    )


    # Vehicle Specifications
    specs = relationship(
        "VehicleSpec",
        back_populates="vehicle"
    )


    # Vehicle Ratings
    ratings = relationship(
        "VehicleRating",
        back_populates="vehicle"
    )


    # Vehicle Reviews
    reviews = relationship(
        "VehicleReview",
        back_populates="vehicle"
    )


    # Vehicle Prices
    prices = relationship(
        "VehiclePrice",
        back_populates="vehicle"
    )


    # Vehicle SEO
    seo = relationship(
        "VehicleSEO",
        back_populates="vehicle"
    )


    # AI Vehicle Score
    ai_score = relationship(
        "AIVehicleScore",
        back_populates="vehicle",
        uselist=False
    )