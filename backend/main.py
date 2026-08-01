from fastapi import FastAPI

from app.routes.health_router import health_router

app = FastAPI(title="KafkaScope API")

app.include_router(health_router, prefix="/api")
