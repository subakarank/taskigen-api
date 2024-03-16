from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime,UTC
from models.base import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  name = Column(String(150), nullable=False)
  email = Column(String(100), unique=True, index=True, nullable=False)
  password = Column(String(50), nullable=False)
  status = Column(String(15), nullable=False)
  created_at = Column(DateTime, default=datetime.now(UTC), nullable=False)
  updated_at = Column(DateTime, nullable=True, onupdate=datetime.now(UTC))
  deleted_at = Column(DateTime, nullable=True)