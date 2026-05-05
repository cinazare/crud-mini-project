from sqlmodel import create_engine
from app.config import DATABASE_URL
from sqlmodel import Field, Session, SQLModel, create_engine, select

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def create_tables():
    SQLModel.metadata.create_all(engine)