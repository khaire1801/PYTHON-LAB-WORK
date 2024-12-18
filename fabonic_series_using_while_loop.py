# Input: number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1
count = 0

# Loop until the count reaches the specified number of terms
while count < n:
    print(a, end=" ")  # Print the current term
    a, b = b, a + b  # Update the terms for the next in the sequence
    count += 1  # Increment the count

print()  # For a newline after the series
