from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.db.base import Base


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer)

    event = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )