Marks = [45,67,84,32,76,50]
high = Marks[0]
low = Marks[0]
passed = 0
passed_mark=[]
Total = 0

for mar in Marks :
 print(mar)    
 if (mar>=50):
     passed+=1
     passed_mark.append(mar)
 if (high<mar):
    high = mar
 if(low>mar):
    low = mar
for pm in passed_mark:
 Total = pm + Total
Total=Total/passed

print("Highest Mark:",high)
print("Lowest Mark:",low)
print("Passed Students :",passed)
print("Passed Students Marks :",passed_mark)
print ("avarage of ",Total)


