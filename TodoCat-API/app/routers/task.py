from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=schemas.TaskResponse, status_code=201)
def add_task(task: schemas.CreateTaskReqeust, db: Annotated[Session, Depends(get_db)]):
    new_task = models.Task(
        content=task.content,
        done=task.done
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("", response_model=list[schemas.TaskResponse], status_code=200)
def get_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.query(models.Task).all()
    return tasks

@router.delete("/{id}", status_code=200)
def delete_task(id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return None