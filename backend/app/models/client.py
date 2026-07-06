from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean

from app.db.base import Base


class Client(Base):

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    age = Column(Integer)

    city = Column(String)

    salary = Column(Float)

    married = Column(Boolean)

    children = Column(Integer)

    sip_amount = Column(Float)

    nominee = Column(String)