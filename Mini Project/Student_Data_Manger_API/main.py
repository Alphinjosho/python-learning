from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students=[]

class Student (BaseModel):
    name:str
    age:int
    course:str
    college:str

@app.get("/")
def home():
    return{
        "message":"Student Data Manager API"
    }
@app.post("/students")
def add_student(new_student:Student):
    students.append(new_student)
    return {
        "name":new_student.name,
        "age": new_student.age,
        "course":new_student.course,
        "college":new_student.college,
        }
@app.get("/students")
def get_students():
    return students 

@app.get("/students/{student_id}")
def get_students(student_id:int):
    return students[student_id]
    
@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:Student):
    students[student_id]=updated_student 
    return updated_student 

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    students.pop(student_id)
    return {
        "message":"Student deleted sucessfully"
    }