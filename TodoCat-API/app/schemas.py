from typing import Annotated
from pydantic import BaseModel, Field

class CreateTaskReqeust(BaseModel):
    content: Annotated[str, Field(max_length=500)]
    done: bool = False

class UpdateTaskReqeust(BaseModel):
    done: bool

class TaskResponse(BaseModel):
    id: int
    content: str
    done: bool