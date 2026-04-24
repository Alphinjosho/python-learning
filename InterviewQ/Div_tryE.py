def div_tryE():
    result = 0
    print("Enter Two Numbers")
    num1 = int (input())
    num2 = int (input())

    try: 
        result = num1 / num2
        print("The Result :",result)
    except:
       print("Second Number Should not Zero")

div_tryE()