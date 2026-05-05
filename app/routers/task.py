from fastapi import APIRouter


router = APIRouter(
    prefix='/task'
)

@router.get('/test/')
def test():
    pass