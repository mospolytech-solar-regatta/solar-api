from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship

from store.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    surname = Column(String)


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False)
    controller_id = Column(Integer, ForeignKey("controllers.id"))
    data = Column(JSON)


class Controller(Base):
    __tablename__ = "controllers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    runtime_id = Column(String)
    telemetry = relationship("Telemetry", backref='controller')
