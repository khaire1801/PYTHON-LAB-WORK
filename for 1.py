#syntax:
'''
for i in range (start,end,step):
'''
for i in range(1,15,2):
    print(i)
print("---------____________")


#WAP to print even numbers between 1 and 20

for i in range(1,21):
    if i%2==0:
        print(i)


#WAP to add number present in the list

num=[23,34,21,4,5]
total=0
for i in num:
    total+=i #total=total+i
print("the total is",total)
