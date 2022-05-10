from datetime import datetime

from sqlalchemy import desc
from sqlalchemy.orm import Session

from store.models import models
from store.schemas.schemas import TelemetryCreate


def get_telemetry(db: Session, controller_id: int,
                  time_from: datetime, time_until: datetime = None):
    res = db.query(models.Telemetry).filter(
        models.Telemetry.controller_id == controller_id)\
        .filter(models.Telemetry.created_at >= time_from)
    if time_until is not None:
        res = res.filter(models.Telemetry.created_at <= time_until)
    return res.all()


def get_last_telemetry(db: Session, controller_id: int):
    res = db.query(models.Telemetry).filter(
        models.Telemetry.controller_id == controller_id)\
        .order_by(desc(models.Telemetry.created_at))
    return res.first()


def create_telemetry(db: Session, data: TelemetryCreate):
    db_telemetry = models.Telemetry(**data.dict())
    db_telemetry.created_at = datetime.now()
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry
