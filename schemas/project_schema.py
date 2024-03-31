from pydantic import BaseModel, Field

class CreateProjectSchema(BaseModel):
    name: str = Field(title='Project name')
    description: str = Field(title="Project Description")

