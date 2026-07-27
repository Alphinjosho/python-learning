from fastapi import FastAPI
from database import engine,Base
import models
from database import SessionLocal
import schemas

Base.metadata.create_all(bind= engine)

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Hello"}

@app.post("/students")
def create_student(student:schemas.StudentCreate):
    student_db = models.Student(
        name=student.name,
        age=student.age,
        course=student.course
    )
    db=SessionLocal()
    db.add(student_db)
    db.commit()
    db.refresh(student_db)
    db.close()
    return student_db

# @app.get("/students")
# def get_student():