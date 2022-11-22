from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
import os

DATABASE = "postgresql"
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
HOST = os.environ.get("POSTGRES_HOST")
NAME = os.environ.get("POSTGRES_NAME")
SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, NAME
)
print(f"urldata:{SQLALCHEMY_DATABASE_URL}")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

sessionlocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    try:
        db_session = sessionlocal()
        yield db_session
    finally:
        db_session.close()