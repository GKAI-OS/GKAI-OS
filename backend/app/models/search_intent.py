from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class SearchIntent(Base):

    __tablename__ = "search_intents"


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


    query = Column(
        String,
        nullable=False
    )


    language = Column(
        String,
        nullable=False
    )


    intent_type = Column(
        String,
        nullable=False
    )


    search_count = Column(
        Integer,
        default=0
    )


    trend_score = Column(
        Integer,
        default=0
    )


    source = Column(
        String,
        nullable=True
    )


    vehicle = relationship(
        "Vehicle",
        backref="search_intents"
    )