from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.database.connection import SessionLocal
from app.crud import task as crud_task
from app.database.connection import get_db
from app.models.user import User
from app.utils.jwt import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskOut)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_task.create_task(db, task_data, current_user.id)

@router.get("/", response_model=list[TaskOut])
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_task.get_tasks_for_user(db, current_user.id)

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud_task.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = crud_task.update_user_task(db, task_id, task_data, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud_task.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
