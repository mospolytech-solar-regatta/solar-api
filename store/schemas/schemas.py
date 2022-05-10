from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class TelemetryBase(BaseModel):
    created_at: datetime
    controller_watts: int
    time_to_go: int
    controller_volts: float
    MPPT_volts: float
    MPPT_watts: float
    motor_temp: float
    motor_revols: float
    speed: Optional[float]
    position_lat: float
    position_lng: float
    distance_travelled: Optional[float]
    laps: Optional[int]
    lap_point_lat: Optional[float]
    lap_point_lng: Optional[float]


class TelemetryCreate(TelemetryBase):
    pass


class Telemetry(TelemetryBase):
    id: int

    class Config:
        orm_mode = True


class ControllerBase(BaseModel):
    name: str
    runtime_id: Optional[str]


class Controller(ControllerBase):
    id: int
    telemetry: List[Telemetry]

    class Config:
        orm_mode = True


class ControllerCreate(ControllerBase):
    pass
