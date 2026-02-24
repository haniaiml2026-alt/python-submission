# Program 20: Number System Functions with Menu
# This program provides a menu-driven interface to perform
# various number system operations like factorial, prime check,
# Fibonacci, sum of digits, reverse number, Armstrong check,
# GCD, LCM, and perfect number check.

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Not defined"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Function to check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Function to get nth Fibonacci number
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# Function to calculate sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# Function to reverse a number
def reverse_number(n):
    return int(str(n)[::-1])

# Function to check if number is Armstrong
def is_armstrong(n):
    power = len(str(n))
    total = sum(int(d)**power for d in str(n))
    return total == n

# Function to calculate GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate LCM
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# Function to check if number is perfect
def is_perfect_number(n):
    if n <= 1:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

# Menu-driven interface
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "10":
            print("Exiting...")
            break

        elif choice == "1":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print("Prime:" , "Yes" if is_prime(n) else "No")

        elif choice == "3":
            n = int(input("Enter position: "))
            print("Fibonacci number:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print("Armstrong:" , "Yes" if is_armstrong(n) else "No")

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Perfect number:" , "Yes" if is_perfect_number(n) else "No")

        else:
            print("Invalid choice")

# Run the number system menu
math_menu()