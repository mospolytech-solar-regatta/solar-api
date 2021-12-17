from fastapi import FastAPI

from app.routers import telemetry, controller

app = FastAPI()

app.include_router(telemetry.router)
app.include_router(controller.router)
