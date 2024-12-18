num = int(input("Enter The Number : ")) #Take value from user
fact=1
ori_num = num   #Take value from user in convert to ori_num

while num > 1:
    fact = fact * num
    num = num - 1
print("Factorial Number : ",fact)   # Print the statement
