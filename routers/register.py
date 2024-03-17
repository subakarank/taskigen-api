from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.register import register_schema
from models.database import get_db
from crud.user_crud import create_user


router = APIRouter()

@router.post('/register', response_model = register_schema.RegisterResponse)
async def register(user: register_schema.Register, db: Session = Depends(get_db) ):
  user_response = create_user(db = db, user_data = user)
  return user_response