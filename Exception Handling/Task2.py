try:
    number1=int(input("Enter a number:"))
    number2=int(input("Enter other Number:"))
    answer = number1/number2
    print(answer)
except  ZeroDivisionError:
     print("0 cannot div")
