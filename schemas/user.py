from pydantic import BaseModel
from datetime import datetime
from typing import Annotated


class User(BaseModel):
  email: str
  name: str
  password: str 
  status: str
  created_at: Annotated[datetime,  None] = None
  updated_at: Annotated[datetime, None] = None
  deleted_at: Annotated[datetime, None] = None 



