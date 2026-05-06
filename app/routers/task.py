from fastapi import APIRouter, Depends, responses
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
    if result == None:
        return responses.JSONResponse(status_code=404, content={'message':'not found'})
    return result

@router.delete('/{task_id}', response_model=Task)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    #validation
    result = delete(id=task_id, session=session, _type=MODULE_TYPE)
    if result == None:
        return responses.JSONResponse(status_code=404, content={'message':'not found'})
    return result

@router.post('/')
def create_task(task: Task, session: Session = Depends(get_session)):
    #validation
    result = create(session=session, entity=task)
    return result


@router.patch('/{task_id}', response_class=Task)
def update_task(task_id: int, task: Task ,session: Session = Depends(get_session)):
    #validation
    result = update(id=task_id, _type=MODULE_TYPE, session=session, entity=task)    
    if result == None:
        return responses.JSONResponse(status_code=404, content={'message':'not found'})
    return result
    