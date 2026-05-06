from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.models import Task
from app.crud import get, create, update, delete


MODULE_TYPE = Task

router = APIRouter(
    prefix=f"/tasks"
)

@router.get('/health/')
def test():
    return {"message":"this is server working"}

@router.get('/', response_model=list[Task])
def get_tasks(session: Session = Depends(get_session)):
    #validation
    result = get(session=session, _type=MODULE_TYPE)
    return result

@router.get('/{task_id}', response_model=Task)
def get_task(task_id: int, session: Session = Depends(get_session)):
    #validation
    result = get(session=session, _type=MODULE_TYPE, id=task_id)
    return result

@router.delete('/{task_id}')
def delete_task(task_id: int, session: Session = Depends(get_session)):
    #validation
    delete(task_id=task_id, session=session, _type=MODULE_TYPE)


@router.post('/')
def create_task(task: Task, session: Session = Depends(get_session)):
    #validation
    print('in the create_task')
    create(session=session, entity=task)
    return "ok"


# @router.put('/{task_id}')
# def update_task(task_id: int, session: Session = Depends(get_session)):
#     #validation
#     return update(id=task_id, _type=MODULE_TYPE, session=session, entity=Task)