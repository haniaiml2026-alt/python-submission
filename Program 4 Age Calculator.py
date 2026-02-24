# Program 4: Age Calculator
# This program calculates a person's age based on their birth year
# and provides the age in months, days, hours, minutes, and also
# the number of years left until they turn 100.

# Asking user for birth year
birth_year = int(input("Enter your birth year: "))

# Current year (can be updated manually if needed)
current_year = 2026

# Calculating age
age = current_year - birth_year           # Age in years
months = age * 12                         # Age in months
days = age * 365                           # Approximate age in days
hours = days * 24                          # Age in hours
minutes = hours * 60                       # Age in minutes
years_left = 100 - age                     # Years remaining until age 100

# Displaying results
print("\nAge Details:")
print("Current age:", age, "years")
print("Age in months:", months)
print("Age in days:", days)
print("Age in hours:", hours)
print("Age in minutes:", minutes)
print("Years until age 100:", years_left)