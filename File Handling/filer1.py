file = open("student.txt","r")
content = file.read()
print(content)
file.close()

# with open("student.txt","r")as file:
#     print(file.read())                  this is used to remove file.close()