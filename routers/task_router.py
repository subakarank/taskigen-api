from fastapi import APIRouter, Depends
from schemas.task_schema import CreateTaskSchema
from dependencies.auth import get_authenticated_user
from enums.priority_enum import PriorityEnum
from enums.task_status_enum import TaskStatusEnum
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post('/task/create')
async def create_task(task: CreateTaskSchema, user = Depends(get_authenticated_user)):
    data = jsonable_encoder(task)
    priority_label = PriorityEnum(task.priority).label 
    task_status = TaskStatusEnum(task.status).label 
    data.update({'priority': priority_label, 'status': task_status}) 
    return data