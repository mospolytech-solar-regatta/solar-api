from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from store import telemetry
from store.schemas.schemas import TelemetryCreate

router = APIRouter(
    prefix='/telemetry',
    tags=['telemetry']
)


@router.get('/')
def get_telemetry(controller_id: int, time_from: datetime, time_until: datetime = None,
                  db: Session = Depends(get_db)):
    return telemetry.get_telemetry(db, controller_id, time_from, time_until)


@router.post('/')
def create_telemetry(req: TelemetryCreate, db: Session = Depends(get_db)):
    return telemetry.create_telemetry(db, req)
