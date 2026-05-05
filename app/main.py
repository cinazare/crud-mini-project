from fastapi import FastAPI
from app.database import create_tables


def lifespan(app: FastAPI):
    create_tables()  
    yield            

app = FastAPI(lifespan=lifespan)