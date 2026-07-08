from student import Student

students=[]

def add_student():
    name=(input("Enter Student name: "))
    age=int(input("Enter Student age: "))
    course=(input("Enter Student course: "))
    student = Student(name,age,course)
    students.append(student)

def view_student():
     for student in students:
        print("Name: ",student.name)
        print("Age: ",student.age)
        print("Course: ",student.course)

def search_student():
     name=input("Enter the name: ")

def delete_student():
    print("this is for Delete")

def exit_program():
    print("for Exit")

print ("1:Add Student\n2:view Student \n3:Search Student \n4:Exit")
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
   exit_program()