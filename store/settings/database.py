import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "public")
    return f"postgresql://{user}:{password}@{server}/{db}"


engine = create_engine(
    get_url()
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
