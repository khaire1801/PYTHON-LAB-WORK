def determine_class(age):
    if 2 <= age < 3:
        return "Eligible for Playgroup"
    elif 3 <= age < 4:
        return "Eligible for Nursery"
    elif 4 <= age < 5:
        return "Eligible for Jr. KG"
    elif 5 <= age < 6:
        return "Eligible for Sr. KG"
    else:
        return "Not eligible for Playgroup, Nursery, Jr. KG, or Sr. KG"

# Get age input from the user
try:
    age = float(input("Enter the child's age in years: "))
# Input from user
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    else:
# Determine the class eligibility
        result = determine_class(age)  
 # Print the result
        print(result) 
except ValueError:
    print("Invalid input. Please enter a numerical value for the age.")
