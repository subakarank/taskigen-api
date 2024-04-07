from pydantic import BaseModel, Field
from datetime import datetime
from enums.priority_enum import PriorityEnum
from enums.task_status_enum import TaskStatusEnum
from typing import Optional

class CreateTaskSchema(BaseModel):
    title: str = Field(title="Name of the task")
    description: str | None 
    priority: PriorityEnum
    status: TaskStatusEnum
    owner_id: int 
    creator_id: int 
    project_id: int
    start_date: datetime | None = Field(title="starting date of the task")
    target_date: datetime | None = Field(title="starting date of the task")







