from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.db.base import Base


class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer)

    advisor = Column(String)

    result = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )