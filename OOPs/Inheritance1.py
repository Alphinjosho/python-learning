class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(person):
    pass
student1=Student("Alphin",21)

print(student1.name)
print(student1.age)

