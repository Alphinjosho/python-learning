student = {
   "name": "Alphin",
   "age": 20
}

print ("Print a key ")
word = str (input())

try:
     student[word]
     print("key is avilabel")
except :
    print("This key is not in this Dictionary ")