from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, task_data: TaskCreate, user_id: int):
    task = Task(**task_data.dict(), user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_all_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()

def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    for key, value in task_data.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task

def get_tasks_for_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task_by_id_for_user(db: Session, task_id: int, user_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()

def update_user_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: int):
    task = get_task_by_id_for_user(db, task_id, user_id)
    if not task:
        return None  # or raise HTTPException

    for key, value in task_data.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

def delete_user_task(db: Session, task_id: int, user_id: int):
    task = get_task_by_id_for_user(db, task_id, user_id)
    if not task:
        return None  # or raise HTTPException

    db.delete(task)
    db.commit()
    return True
