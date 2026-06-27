import random 

secret_number = random.randint(1,100)

print("Guess a number between 1 and 100")
 

i=0
while i<5:
    print("You have ",5-i,"chances")
    guess=int(input())
    if guess>secret_number:
     print("Too high! Try a smaller number.")
 
    elif guess<secret_number:
     print("Too low! Try a bigger number.")

    else:
     print("Yeahhh that is the number:",secret_number)
     break
    i+=1 
    if i==5:
       print("Game Over! The correct number was", secret_number) 