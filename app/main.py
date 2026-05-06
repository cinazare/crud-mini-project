from fastapi import FastAPI
from app.database import create_tables
from app.routers.task import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield            

app = FastAPI(lifespan=lifespan)

app.include_router(router)