from fastapi import APIRouter

router = APIRouter()

@router.get('/login')
def login():
  return {"message" : "This is login page"}