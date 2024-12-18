#WAP to print first 20 even numbers in reverse order
# Initialize variables
even_numbers = []

# Generate the first 20 even numbers
for i in range(1, 21):
    even_numbers.append(i * 2)

# Reverse the list of even numbers
even_numbers.reverse()

# Print the first 20 even numbers in reverse order
print("The first 20 even numbers in reverse order are:")
for num in even_numbers:
    print(num)
