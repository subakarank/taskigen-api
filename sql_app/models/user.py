from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  name = Column(String, )
  email = Column(String, unique=True, index=True)
  password = Column(String)
  created_at = Column(TIMESTAMP)