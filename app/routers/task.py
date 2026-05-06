from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from app.models import Task


router = APIRouter(
    prefix="/task"
)

@router.get('/health/')
def test():
    return {"message":"this is server working"}

@router.get('/')
def get_tasks(session: Session = Depends(get_session)):
    pass

@router.get('/{task_id}')
def get_task(task_id: id, session: Session = Depends(get_session)):
    pass

@router.delete('/{task_id}')
def delete_task(task_id: id, session: Session = Depends(get_session)):
    pass

@router.post('/')
def create_task(session: Session = Depends(get_session)):
    pass

@router.put('/{task_id}')
def update_task(task_id: id, session: Session = Depends(get_session)):
    pass