# Program 2: Simple Calculator
# This program takes two numbers from the user and performs basic
# arithmetic operations such as addition, subtraction, multiplication,
# division, modulus, and exponentiation.

# Taking input from the user
# float() is used to allow both integer and decimal values
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing arithmetic calculations
add_result = num1 + num2      # Addition of two numbers
sub_result = num1 - num2      # Subtraction of two numbers
mul_result = num1 * num2      # Multiplication of two numbers
div_result = num1 / num2      # Division of two numbers
mod_result = num1 % num2      # Modulus gives remainder
exp_result = num1 ** num2     # Exponentiation (num1 raised to power num2)

# Displaying results
# round() is used to limit division result to 2 decimal places
print("\nResults:")
print(num1, "+", num2, "=", add_result)
print(num1, "-", num2, "=", sub_result)
print(num1, "*", num2, "=", mul_result)
print(num1, "/", num2, "=", round(div_result, 2))
print(num1, "%", num2, "=", mod_result)
print(num1, "^", num2, "=", exp_result)