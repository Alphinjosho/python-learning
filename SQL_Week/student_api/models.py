from sqlalchemy import Column,Integer,String
from database import Base

class Student(Base): 
    __tablename__="students"
    id = Column(Integer,primary_key= True,index= True)
    name = Column (String , nullable= False)
    age = Column(Integer , nullable= False)
    course=Column(String, nullable=False)
class User(Base): 
    __tablename__="users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column (String , nullable = False)
    email = Column (String , nullable = False)
    hashed_password = Column (String , nullable = False)
