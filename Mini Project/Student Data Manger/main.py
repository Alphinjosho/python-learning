from student import Student
import json

students=[]

def add_student():
    name=(input("Enter Student name: "))
    age=int(input("Enter Student age: "))
    course=(input("Enter Student course: "))
    student = Student(name,age,course)
    students.append(student)
    save_students()

def view_student():
     for student in students:
        print("Name: ",student.name)
        print("Age: ",student.age)
        print("Course: ",student.course)

def search_student():
    name=input("Enter the name: ")
    found = False

    for student in students:
        if name==student.name:   
            found=True
            print("Name:", student.name)
            print("Age:", student.age)
            print("Course:", student.course)
    if not found:
        print("Student Not Fount")      
    
def delete_student():
     name=input("Enter the name: ")
     for student in students:
         if name==student.name:
             students.remove(student)
             print("Student deleted successfully.")
             break
     else:
        print("Student is not found")
     save_students()    

def edit_student():
    name=input("Enter the name: ")
    for student in students:
            if name==student.name:
             new_age=int (input("Enter New age"))
             student.age=new_age
             new_course=input("Enter New course")
             student.course=new_course
             print("Student Edit successfully.")
             break
    else:
         print ("Student not found")
    save_students()
 
def save_students():
    data=[]     
    for student in students:
        student_data={
            "name": student.name,
            "age": student.age,
            "course":student.course
        } 
        data.append(student_data)

    with open ("students.json","w")as file:
        json.dump(data,file)

def load_students():
    with open ("students.json","r")as file:
        data = json.load(file)
    for item in data:
        student=Student(
            item["name"],
            item["age"],
            item["course"]
        )
        students.append(student)

load_students()
print ("1:Add Student\n2:view Student\n3:Search Student\n4:Delete Student\n5:Edit student")
try:
    number=int(input("Enter your Choice:"))
except ValueError:
    print("Invalid")

if number == 1:
    add_student()
 
elif number==2:
  view_student()

elif number==3:
 search_student()

elif number==4:
   delete_student()

elif number==5:
   edit_student()