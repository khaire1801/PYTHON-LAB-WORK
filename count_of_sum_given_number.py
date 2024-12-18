n=int(input("Enter Number : ")) # Take value from user
sum1=0
num=abs(n)  # convert into absolute value
while num>0:
    sum1=sum1+num%10
    num=num//10

print("Sum of Digits : ",sum1) # print the statement
