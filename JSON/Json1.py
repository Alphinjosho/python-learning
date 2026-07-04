import json

student = {
    "name": "Alphin",
    "age": 21,
    "course": "AI Backend engineer"
}

with open("student.json", "w") as file:
    json.dump(student, file)