from pydantic import BaseModel, Field
from datetime import datetime
from schemas.user_schema import UserSchema, ProjectUserSchema
from typing import Optional

class CreateProjectSchema(BaseModel):
    name: str = Field(title='Project name')
    description: str = Field(title="Project Description")

class ViewProjectSchema(BaseModel):
    id: int = Field(title="ID of the project")
    name: str = Field(title='Project name')
    description: str = Field(title="Project Description")
    user: UserSchema
    created_at: datetime = Field(title="created date and time ", serialization_alias='createdAt')
    updated_at: Optional[datetime] = Field(title="updated date and time", serialization_alias='updatedAt')

class ListProjectSchema(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime = Field(title="created date and time ", serialization_alias='createdAt')
    updated_at: Optional[datetime] = Field(title="updated date and time", serialization_alias='updatedAt')
    user: ProjectUserSchema


