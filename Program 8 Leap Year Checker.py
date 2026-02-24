# Program 8: Leap Year Checker
# This program checks whether a given year is a leap year
# and provides an explanation of why it is or isn't a leap year.

# Asking user to enter a year
yr = int(input("Enter the year to check: "))

# Initialize default values
leap_flag = False   # Flag to indicate if year is leap
message = ""        # Message explaining the reason

# Checking leap year conditions
if yr % 4 == 0 and yr % 100 != 0:
    leap_flag = True
    message = "Year is divisible by 4 and not divisible by 100"

elif yr % 400 == 0:
    leap_flag = True
    message = "Year is divisible by 400"

else:
    leap_flag = False
    message = "Year does not satisfy leap year conditions"

# Displaying output
print("\nEntered Year:", yr)

if leap_flag:
    print("This is a Leap Year")
else:
    print("This is NOT a Leap Year")

print("Explanation:", message)