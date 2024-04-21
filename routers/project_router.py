from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.responses import JSONResponse
from typing import Annotated
from sqlalchemy.orm import Session

from dependencies import auth
from models import user_model, project_model
from models.database import get_db
from schemas.project_schema import CreateProjectSchema, ViewProjectSchema, ListProjectSchema
from crud.project_crud import create_project, view_project

router = APIRouter()

@router.post('/project/create', response_model=ViewProjectSchema)
async def create(project: CreateProjectSchema,
                          user: user_model.UserModel = Depends(auth.get_authenticated_user), db: Session =  Depends(get_db)):
    created_project = create_project(db = db, project=project, user=user)
    if(created_project is not None):
        return created_project
    else: 
        return JSONResponse(status_code=201, content = {'message': 'project is not created'})
    
@router.get('/project/{project_id}', response_model=ViewProjectSchema , response_model_exclude=['deleted_at'])
async def view(project_id: Annotated[int, Path(title="project id")],
                user: user_model.UserModel = Depends(auth.get_authenticated_user), db: Session =  Depends(get_db)) -> ViewProjectSchema:
    project = view_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get('/projects')
async def listProjects(user: user_model.UserModel = Depends(auth.get_authenticated_user), db: Session = Depends(get_db)) -> ListProjectSchema:
    
    pass

