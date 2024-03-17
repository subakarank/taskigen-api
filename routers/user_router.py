from fastapi import APIRouter, Depends
from dependencies import auth
from schemas.user_schema import UserSchema
from models.user_model import UserModel

router = APIRouter()

@router.get('/me', response_model=UserSchema)
async def me(user: UserModel = Depends(auth.get_authenticated_user)):
    return user
