#WAP to get tabels rom 5 to 10
# Print multiplication tables from 5 to 10
for number in range(5, 11):
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
