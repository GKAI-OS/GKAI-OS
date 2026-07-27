from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class VehicleSEO(Base):

    __tablename__ = "vehicle_seo"


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


    meta_title = Column(
        String,
        nullable=False
    )


    meta_description = Column(
        String,
        nullable=False
    )


    seo_slug = Column(
        String,
        unique=True,
        nullable=False
    )


    primary_keyword = Column(
        String,
        nullable=True
    )


    secondary_keywords = Column(
        String,
        nullable=True
    )


    search_intent = Column(
        String,
        nullable=True
    )


    schema_type = Column(
        String,
        default="Vehicle"
    )


    faq_schema = Column(
        String,
        nullable=True
    )


    review_schema = Column(
        String,
        nullable=True
    )


    last_updated = Column(
        DateTime,
        default=datetime.utcnow
    )