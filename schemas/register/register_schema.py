from pydantic import BaseModel
from enums.user_status import UserStatus
from typing import Annotated



class Register(BaseModel):
  email: str
  name: str
  password: str
  status: Annotated[UserStatus, None] = UserStatus.REGISTERED

class RegisterResponse(BaseModel):
  email: str
  name: str
  status: UserStatus
  