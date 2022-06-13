from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"Hello": "This is the service for reading database."}

@app.get("/read/{npm}")
async def read(npm: str, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, npm)
    return {
        "status": "OK",
        'npm': db_student.npm,
        'nama': db_student.name
    }