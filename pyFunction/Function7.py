def total(*numbers):
   
    answer = 0
    for number in numbers:
        answer=number+answer
    print(answer)
total(10,20,43,23,33)