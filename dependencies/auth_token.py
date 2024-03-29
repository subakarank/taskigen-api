from pydantic import BaseModel 
from schemas.user_schema import UserSchema

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class TokenSchema(BaseModel):
  token: str
  token_type: str
  expires_in: int 

class TokenUserSchema(BaseModel):
  name: str
  email: str
  sub: str 

class TokenData(BaseModel):
  username: str | None = None

class AuthResponseSchema(BaseModel):
  token: str
  user: TokenUserSchema
