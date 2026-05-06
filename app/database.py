from sqlmodel import create_engine
from app.config import DATABASE_URL
from sqlmodel import SQLModel, create_engine, Session

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session