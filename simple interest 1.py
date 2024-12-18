# Take inputs from the user
P = float(input("Enter the principal amount (Rs.): "))
R = float(input("Enter the rate of interest per year (%): "))
T = float(input("Enter the time period in years: "))

# Calculate simple interest
SI = (P * R * T) / 100

# Display the result
print(f"The Simple Interest on Rs.{P} for {T} years at {R}% per year is Rs.{SI}.")
