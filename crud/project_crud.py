# crud/project_crud.py

from sqlalchemy.orm import Session
from datetime import datetime, UTC
from models.project_model import ProjectModel
from models.user_model import UserModel
from schemas.project_schema import CreateProjectSchema


def create_project(db: Session, project: CreateProjectSchema, user: UserModel) -> ProjectModel:
    db_project = ProjectModel(name = project.name, description = project.description,
                              user_id = user.id,
                               created_at = datetime.now(UTC))
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

