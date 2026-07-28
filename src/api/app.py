from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.api.routes import router
from src.api.database import create_logs_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_logs_table()
    yield


app = FastAPI(
    title="LifeOS API",
    version="1.0",
    lifespan=lifespan
)

app.include_router(router)