from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Date
from datetime import datetime, UTC
from sqlalchemy.orm import relationship

from models.base_model import Base
from models.user_model import UserModel
from models.project_model import ProjectModel


class TaskModel(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, )
    title =  Column(String(300), nullable=False)
    description = Column(Text, nullable=True)
    priority = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)
    project_id = Column(Integer, ForeignKey(ProjectModel.id, ondelete='CASCADE'), nullable=False)
    owner_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
    creator_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
    
    start_date = Column(Date, nullable=True)
    target_date = Column(Date, nullable=True)
    uploads = Column(String(1000), nullable=True)
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=None, nullable=True, onupdate=datetime.now(UTC) )
    deleted_at = Column(DateTime, nullable=True, default=None)

    owner = relationship("UserModel", foreign_keys=[owner_id])
    creator = relationship("UserModel", foreign_keys=[creator_id])
    project = relationship("ProjectModel", foreign_keys=[project_id])