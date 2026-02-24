# Program 12: Multiplication Table Generator
# This program generates and displays the multiplication table
# of a given number up to a specified range.

# Taking input from user
num = int(input("Enter number: "))           # Number for which table is needed
limit = int(input("Enter range (end): "))    # Up to which multiplier

print("\nMultiplication Table of", num)

# Loop to print the multiplication table
for i in range(1, limit + 1):
    result = num * i
    print(num, "x", i, "=", result)