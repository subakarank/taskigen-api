from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
from enums.user_status import UserStatus


class UserSchema(BaseModel):
  email: str
  name: str
  status: Annotated[UserStatus, None] = None




