from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from sqlalchemy.orm import Session

from dependencies import auth
from models import user_model, project_model
from models.database import get_db
from schemas.project_schema import CreateProjectSchema
from crud.project_crud import create_project

router = APIRouter()

@router.post('/project/create')
async def create(project: CreateProjectSchema,
                          user: user_model.UserModel = Depends(auth.get_authenticated_user), db: Session =  Depends(get_db)):
    created_project = create_project(db = db, project=project, user=user)
    if(created_project is not None):
        return JSONResponse(status_code=200, content = {'message': 'Successfully created'})
    else: 
        return JSONResponse(status_code=201, content = {'message': 'project is not created'})
