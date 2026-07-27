from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class ModuleName(Base):

    __tablename__ = "module_names"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        unique=True,
        nullable=False
    )


    description = Column(
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


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )