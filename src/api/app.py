from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="LifeOS API",
    version="1.0.0",
    description="Behavioral Analytics Backend"
)

app.include_router(router)