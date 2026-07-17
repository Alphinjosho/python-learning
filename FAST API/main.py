from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name:str
    age:int
    course:str
    college:str


@app.get("/")
def home(): 
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello")
def hello():
    return {"message":"Hello Alphin"}

@app.get("/student")
def student():
    return {
        "name":"Alphin Josho",
        "age":21,
        "course":"Ai backend enginer",
        "collage":"IGNOU-SH"
    }
@app.get("/skills")
def skills():
    return{
        "name":"Alphin Josho",
        "skills" : ["Python","SQL","Docker","Problem Sloving","FastAPI"]
    }

@app.get("/projects")
def project():
    return{
        "project1": {
            "project_name": "Student management API",
            "technology":["FastAPI","Python"],
            "status":"completed"
            },
        "project2": {
            "project_name": "Smart Notes App",
            "technology":["FastAPI","React"],
            "status":"planning"
            },
        "project3": {
            "project_name": "AI Student Assistant",
            "technology":["FastAPI","LLM","LangChain"],
            "status":"futuer Project"
            }
    }
@app.post("/student")
def add_student(new_student:Student):

    return{ 
         "name":new_student.name,
         "age":new_student.age,
         "course":new_student.course
    } 

@app.get("/student/{id}")
def get_student(student_id:int):
    return{
        "student_id" : student_id
    }
@app.get("/student")
def get_student(course:str):
    return{
        "course":course
    }
@app.put("/student/{id}")
def update_student(student_id:int,new_student:Student):
    return{
        "student_id":student_id,
        "name":new_student.name,
        "age":new_student.age,
        "course":new_student.course
    }
@app.delete("/student/{id}")
def delete_student(student_id:int):
    return{
        "student_id":student_id,
        "message": "successfuly deleted"
    }