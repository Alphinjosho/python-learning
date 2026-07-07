import student
def add_student():
    name=(input("Enter Student name: "))
    age=int(input("Enter Student age: "))
    course=(input("Enter Student course: "))

def view_student():
    print("This is for view student")

def search_student():
    print("This is for search student")

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