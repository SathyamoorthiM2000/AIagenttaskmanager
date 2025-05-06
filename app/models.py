from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base  

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    place = Column(String, nullable=True)
    time = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Task(title={self.title}, description={self.description})>"
