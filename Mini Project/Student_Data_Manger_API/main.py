from fastapi import FastAPI

app = FastAPI()

class Student (BaseModel):
    name:str
    age:int
    course:str
    collage:str

@app.get("/")
def home():
    return{
        "message":"Student Data Manager API"
    }
@app.post("/Student")
def add_student(new_student:Student):
    return{
         new_student.name:name,
         new_student.age,
         new_student.course,
         new_student.collage,
         
    }