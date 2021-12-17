from sqlalchemy.orm import Session

from store.models import models
from store.schemas.schemas import ControllerCreate


def get_controllers(db: Session):
    return db.query(models.Controller).all()


def get_controller(db: Session, id: int):
    return db.query(models.Controller).filter(models.Controller.id == id).first()


def create_controller(db: Session, data: ControllerCreate) -> models.Controller:
    db_controller = models.Controller(**data.dict())
    db.add(db_controller)
    db.commit()
    db.refresh(db_controller)
    return db_controller
