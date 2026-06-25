scores = (32, 64, 12, 89, 45)

check = scores[0]
for mark in scores:
    if check>=mark:
      check=mark
print("The smallest number is :",check)