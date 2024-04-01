# crud/project_crud.py

from sqlalchemy.orm import Session
from datetime import datetime, UTC
from models.project_model import ProjectModel
from models.user_model import UserModel
from schemas.project_schema import CreateProjectSchema, ViewProjectSchema
from models.database import get_db
from sqlalchemy import Select

def create_project(db: Session, project: CreateProjectSchema, user: UserModel) -> ProjectModel:
    db_project = ProjectModel(name = project.name, description = project.description,
                              user_id = user.id,
                               created_at = datetime.now(UTC))
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# def view_project(db: Session, id: int) -> ViewProjectSchema:
#     project = db.query(ProjectModel).get(id)
#     if project is None:
#         return None  # Handle the case where the project does not exist

#     # Create a dictionary representing the project data
#     project_data = {
#         'name': project.name,
#         'description': project.description,
#         'user': {
#             'name': project.user.name,
#             'email': project.user.email,
#             # Include other user fields as needed
#         },
#         'created_at': project.created_at,
#         'updated_at': project.updated_at
#     }

#     # Validate the project data against the ViewProjectSchema
#     return ViewProjectSchema(**project_data)

def view_project(db: Session, id: int) -> ViewProjectSchema | None :
    stmt = Select(ProjectModel, UserModel.name, UserModel.email, UserModel.status).join(UserModel).where(ProjectModel.id == id)
    project = db.execute(stmt).scalar()
    if project is None:
        return None  # Handle the case where the project does not exist
    # Create a dictionary representing the project data
    project_data = {
        'name': project.name,
        'description': project.description,
        'user': {
            'name': project.user.name,
            'email': project.user.email,
            'status': project.user.status,
        },
        'created_at': project.created_at,
        'updated_at': project.updated_at
    }
    # Validate the project data against the ViewProjectSchema
    return ViewProjectSchema(**project_data)

