from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from datetime import datetime, UTC

from models.base_model import Base
from models.user_model import UserModel


class ProjectModel(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, )
    user_id = Column(Integer, ForeignKey(UserModel.id, ondelete='CASCADE'))
    name =  Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=None, nullable=True, onupdate=datetime.now(UTC) )
    deleted_at = Column(DateTime, nullable=True, default=None)