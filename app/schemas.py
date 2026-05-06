from sqlmodel import SQLModel

class TaskUpdateAndCreate(SQLModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None