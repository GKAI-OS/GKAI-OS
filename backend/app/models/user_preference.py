from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class UserPreference(Base):

    __tablename__ = "user_preferences"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        nullable=False
    )


    preferred_brand = Column(
        String,
        nullable=True
    )


    preferred_category = Column(
        String,
        nullable=True
    )


    budget_range = Column(
        String,
        nullable=True
    )


    fuel_preference = Column(
        String,
        nullable=True
    )


    transmission_preference = Column(
        String,
        nullable=True
    )


    usage_type = Column(
        String,
        nullable=True
    )


    language = Column(
        String,
        nullable=True
    )


    city = Column(
        String,
        nullable=True
    )


    preference_score = Column(
        Integer,
        default=0
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