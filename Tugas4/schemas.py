from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    npm: str

class Student(StudentBase):
    id: int
    
    class Config:
        orm_mode = True
