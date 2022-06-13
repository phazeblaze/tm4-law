from unicodedata import name
from sqlalchemy.orm import Session

from . import models, schemas

# Get student
def get_student(db: Session, npm: str):
    return db.query(models.Student).filter(models.Student.npm == npm).first()

# Create and update student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name = student.name, npm = student.npm)
    e_student = get_student(db, student.npm)
    # if student exists, update
    if (e_student is not None):
        e_student.name = student.name
        db.add(e_student)
        db.commit()
        db.refresh(e_student)
        return e_student

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
