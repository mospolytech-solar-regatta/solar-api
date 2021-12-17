from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from store import controller
from store.schemas import schemas
from store.schemas.schemas import ControllerCreate

router = APIRouter(
    prefix='/controller',
    tags=['controller']
)


@router.get('/', response_model=List[schemas.Controller])
def get_controllers(db: Session = Depends(get_db)):
    return controller.get_controllers(db)


@router.get('/{id}')
def get_controller(id: int, db: Session = Depends(get_db)):
    return controller.get_controller(db, id)


@router.post('/')
def create_controller(req: ControllerCreate, db: Session = Depends(get_db)):
    return controller.create_controller(db, req)
