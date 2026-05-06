from fastapi import APIRouter, Response
from app.crud import test_function


router = APIRouter(
    prefix="/task"
)

@router.get('/health/')
def test():
    return {"message":"this is server working"}