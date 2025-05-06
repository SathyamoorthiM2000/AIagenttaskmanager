from sqlalchemy.orm import Session
from . import models, schemas
from .nlp import extract_place_and_time

def create_task(db: Session, task: schemas.TaskCreate):
    place, time = extract_place_and_time(task.description)
    db_task = models.Task(
        title=task.title, 
        description=task.description,
        place=place,
        time=time
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(task)
    db.commit()
    return task
