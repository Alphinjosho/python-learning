from fastapi import FastAPI,Depends
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

@app.get("/students")
def get_student():
    db=SessionLocal()
    students=db.query(models.Student).all()
    db.close()
    return students

@app.get("/students/{id}")
def get_student(id:int):
        db=SessionLocal()
        student=db.query(models.Student).filter(models.Student.id==id).first()
        db.close()
        return student

@app.put("/students/{id}")
def update_student(id:int,student:schemas.StudentCreate):
    db=SessionLocal()
    student_db=db.query(models.Student).filter(models.Student.id==id).first()
    student_db.name = student.name
    student_db.age = student.age
    student_db.course = student.course
    db.commit()
    db.refresh(student_db)
    db.close()
    return student_db

@app.delete("/students/{id}")
def delete_student(id:int):
    db=SessionLocal()
    student_db=db.query(models.Student).filter(models.Student.id==id).first()
    db.delete(student_db)
    db.commit()
    db.close()
    return  {"message":"student deleted successfully"}

@app.post("/register")
def register_user(
    user:schemas.UserCreate,
    db:Session=Depends(get_db)
    ):

   new_user=models.User(
   username = user.username,
   email = user.email,
   hashed_password = hash_pass(user.password))

   db.add(new_user)
   db.commit()
   db.refresh(new_user)   

   return{"message": "user added"}
   

