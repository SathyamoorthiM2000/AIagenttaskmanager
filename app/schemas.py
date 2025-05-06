from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str

class Task(TaskCreate):
    id: int
    created_at: datetime
    place: str | None = None
    time: datetime | None = None

    class Config:
        orm_mode = True
