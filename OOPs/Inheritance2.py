class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course
student1=Student("Alphin",21,"AI")

print(student1.name)
print(student1.age)
print(student1.course)