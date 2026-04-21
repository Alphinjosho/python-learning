print ("Enter 3 Numbers :")
number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 > number2 and  number1 >number3:
    print(number1," :Is largest Number ")
elif number2 > number1 and  number2 >number3 :
    print(number2," :Is largest Number ")
else :
    print(number3," :Is largest Number ")