tuple_item=()
total_item = int (input("Enter a total number of items"))
for i in  range (total_item):
 user_input=int(input("Enter a number"))
 tuple_item += (user_input,)
 print ("item added to tumpl are",tuple_item)