from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class UserInteraction(Base):

    __tablename__ = "user_interactions"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        nullable=True
    )


    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )


    action_type = Column(
        String,
        nullable=False
    )


    search_query = Column(
        String,
        nullable=True
    )


    language = Column(
        String,
        nullable=True
    )


    session_id = Column(
        String,
        nullable=True
    )


    interest_score = Column(
        Integer,
        default=0
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    vehicle = relationship(
        "Vehicle"
    )