from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key = True)
    name = Column(String)

class Calendar(Base):
    __tablename__ = "calender"
    cal_id = Column(String, primary_key = True)
    user_id = Column(String)
    date = Column(DateTime)
    text = Column(String)
    url = Column(String)