import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from db.base import Base


class Ad(Base):

    __tablename__: str = 'ads'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
    is_active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())


class User(Base):

    __tablename__: str = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)
    email = Column(String, primary_key=True, unique=True)
    name = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
