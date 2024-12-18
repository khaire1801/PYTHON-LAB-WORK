n=int(input("enter number :")) #take value from user
sum1=0
num=abs(n) #convert into absolute value
while num>0:
    sum1=sum1+num%10
    num=num//10

print("sum of digits : ",sum1) #print the statement
