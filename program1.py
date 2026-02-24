# Program 1: Student Bio Card
# This program displays a formatted student bio card using stored student details.

# Variables storing student information
# These variables hold the student's personal and academic details
name = "John Doe"
age = 20
course = "Python Programming"
college = "ABC University"
email = "john@example.com"

# Printing the formatted bio card
# The print statements use box characters to create a card-like structure
print("╔══════════════════════════════════╗")
print("║        STUDENT BIO CARD          ║")
print("╠══════════════════════════════════╣")

# Displaying each field with proper alignment using f-string formatting
# <:23 ensures the text is left aligned within 23 spaces
print(f"║  Name    : {name:<23}║")
print(f"║  Age     : {str(age) + ' years':<23}║")
print(f"║  Course  : {course:<23}║")
print(f"║  College : {college:<23}║")
print(f"║  Email   : {email:<23}║")

# Printing the bottom border of the bio card
print("╚══════════════════════════════════╝")