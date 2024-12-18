n=int(input("Enter Number : "))
count=0
num=abs(n) # Take the Absolute Number
while num > 0:
    num=num//10
    count=count+1 #Count the number one ny one

if n==0: #if then n==0 then it's start to count
    count = 1

print("Count of Number is : ",count)    #print the statement

