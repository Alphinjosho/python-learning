from pydantic import BaseModel

class StudentCreate(BaseModel):
    name:str
    age:int
    course:str

class UserCreate(BaseModel):
    username:str
    email:str
    password:str