from fastapi import FastAPI

from app.routers import telemetry

app = FastAPI()

app.include_router(telemetry.router)
