from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from models.database import get_db

from passlib.context import CryptContext
from jose import JWTError, jwt
from dependencies.auth_token import AuthResponseSchema, TokenUserSchema, TokenSchema, SECRET_KEY, ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
from crud.user_crud import get_user_by_email

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Generate JWT token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    try:
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except JWTError as e:
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Could not create access token",
        ) from e

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_email(db, username)
    if not user or not verify_password(password, user.password):
        return None  # Return None if authentication fails
    return user

@router.post("/login", response_model= AuthResponseSchema)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends(),], db: Session = Depends(get_db)
) -> AuthResponseSchema:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
    )
    user_schema = TokenUserSchema(email=user.email, name=user.name, sub=user.email)
    # token_schema = TokenSchema(token=access_token,
    #                 token_type="bearer",
    #                 expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    return AuthResponseSchema(token=access_token, user=user_schema)