from fastapi import APIRouter, Depends, responses
from sqlmodel import Session
from app.database import get_session
from app.models import Task
from app.crud import get, create, update, delete
from app.schemas import TaskUpdateAndCreate


MODULE_TYPE = Task

router = APIRouter(
    prefix=f"/tasks",
    tags=['Tasks']
)

@router.get('/health/', summary='Check service health')
def test():
    return {"message":"this is server working"}


@router.get('/', response_model=list[Task], summary='Get all the tasks in Tasks table')
def get_tasks(session: Session = Depends(get_session)):
    try:
        result = get(session=session, _type=MODULE_TYPE)
        return result
    except Exception as e:
        return responses.JSONResponse(status_code=500)


@router.get(
    '/{task_id}', 
    response_model=Task, 
    summary='Get one of the tasks in Tasks',
    responses={404:{'message':'not found'}}
)
def get_task(task_id: int, session: Session = Depends(get_session)):
    try:
        result = get(session=session, _type=MODULE_TYPE, id=task_id)
        if result == None:
            return responses.JSONResponse(status_code=404, content={'message':'not found'})
        return result
    except Exception as e:
        return responses.JSONResponse(status_code=500)


@router.delete(
    '/{task_id}', 
    response_model=Task, 
    summary='Delete the task from database',
    responses={404:{'message':'not found'}}
)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    try:
        result = delete(id=task_id, session=session, _type=MODULE_TYPE)
        if result == None:
            return responses.JSONResponse(status_code=404, content={'message':'not found'})
        return result
    except Exception as e:
        return responses.JSONResponse(status_code=500)


@router.post('/', summary='Create a task in database')
def create_task(task: TaskUpdateAndCreate, session: Session = Depends(get_session)):
    try:
        task_object = Task(**task.model_dump())
        result = create(session=session, entity=task_object)
        return result
    
    except Exception as e:
        return responses.JSONResponse(status_code=500)


@router.patch(
    '/{task_id}', 
    response_model=Task, 
    summary='Update one task based on the fields endpoint receives',
    responses={404:{'message':'not found'}}
)
def update_task(task_id: int, task: TaskUpdateAndCreate ,session: Session = Depends(get_session)):
    try:
        task_object = Task(**task.model_dump())
        result = update(id=task_id, _type=MODULE_TYPE, session=session, entity=task_object)    
        if result == None:
            return responses.JSONResponse(status_code=404, content={'message':'not found'})
        return result
    except Exception as e:
        return responses.JSONResponse(status_code=500)
    