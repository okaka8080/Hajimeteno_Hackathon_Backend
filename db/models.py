from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key = True)
    name = Column(String)
