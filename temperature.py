import random #importing random modules to generate rando, numbers

#simulating temperature reading
for i in range (1,11): #10 temperature redings
    temperature = random.randint(20,100)
    print(f"reading {i}:temperature ={temperature}c")
    if temperature>70:
        print("danger! high temperature detected. stopping monitoring.")
        break #stop monitoring when temperature exceeds safe limits
    
