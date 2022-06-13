from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    npm = Column(String)
    name = Column(String)