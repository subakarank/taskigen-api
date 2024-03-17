from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
from enums.user_status import UserStatus


class UserSchema(BaseModel):
  email: str
  name: str
  password: str 
  status: Annotated[UserStatus, None] = UserStatus.REGISTERED
  



