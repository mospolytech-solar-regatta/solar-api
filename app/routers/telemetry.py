from fastapi import APIRouter

router = APIRouter(
    prefix='/telemetry',
    tags=['telemetry']
)


@router.get('/')
def get_telemetry():
    return {}


@router.post('/')
def set_telemetry():
    return {}
