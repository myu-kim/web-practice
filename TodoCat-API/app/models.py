from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    done = Column(Boolean, nullable=False)

# class Cat(Base):
#     __tablename__ = "cats"
#
#     id = Column(Integer, primary_key=True)
#     content = Column(String, nullable=False)
#     done = Column(Boolean, nullable=False)