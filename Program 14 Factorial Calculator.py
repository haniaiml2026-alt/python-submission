# Program 14: Factorial Calculator
# This program calculates the factorial of a non-negative integer
# using a loop and displays the steps of multiplication.

# Taking input from user
num = int(input("Enter a number: "))

# Check for negative number
if num < 0:
    print("Factorial is not defined for negative numbers.")

# Factorial of 0 is 1
elif num == 0:
    print("0! = 1")

else:
    factorial = 1   # To store factorial result
    steps = ""      # To display multiplication steps

    # Loop to calculate factorial and store steps
    for i in range(num, 0, -1):
        factorial *= i
        steps += str(i)
        if i != 1:
            steps += " × "

    # Display result with steps
    print(f"{num}! = {steps} = {factorial}")