# Program 18: Advanced Calculator with Menu
# This program provides a menu-driven calculator for
# addition, subtraction, multiplication, division, modulus, and power.
# It handles division/modulus by zero and allows repeated calculations.

# Define calculator operations
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    return "Cannot divide by zero" if b == 0 else a / b

def modulus(a, b): 
    return "Cannot modulus by zero" if b == 0 else a % b

def power(a, b): 
    return a ** b

# Calculator function with menu
def calculator():
    while True:
        # Display menu
        print("\nCalculator Menu")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        # Take user choice
        choice = input("Enter choice: ")

        # Exit option
        if choice == "7":
            print("Calculator closed")
            break

        # Input numbers
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # Perform selected operation
        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "5":
            print("Result:", modulus(a, b))
        elif choice == "6":
            print("Result:", power(a, b))
        else:
            print("Invalid choice")

# Run calculator
calculator()