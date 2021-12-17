import datetime
from typing import List, Dict, Union, Optional

from pydantic import BaseModel


class TelemetryBase(BaseModel):
    controller_id: int
    data: Dict[str, Union[float, int, str]]


class TelemetryCreate(TelemetryBase):
    pass


class Telemetry(TelemetryBase):
    id: int
    created_at: datetime.datetime

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
