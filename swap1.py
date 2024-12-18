# Take all three inputs in a single line separated by spaces
num1, num2, num3 = input("Enter three numbers separated by spaces: ").split()

# Display the numbers before swapping
print(f"Before swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")

# Swap the first two numbers
num1, num2 = num2, num1

# Display the numbers after swapping
print(f"After swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")
