from fastapi import APIRouter
from schemas import user

router = APIRouter()

@router.post('/register')
def register(user_data: user.User ):
  return user_data