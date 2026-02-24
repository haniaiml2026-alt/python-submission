# Program 15: Prime Number Checker and Prime Range Finder
# This program checks if a single number is prime and also finds
# all prime numbers within a given range.

# Part 1: Check if a single number is prime
num = int(input("Enter a number: "))

# Function to check prime
if num < 2:
    print(num, "is NOT a PRIME number")

elif num == 2:
    print("2 is a PRIME number")

else:
    is_prime = True

    # Loop to check divisibility
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Display result
    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a PRIME number")

# Part 2: Find prime numbers in a range
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers in range:", end=" ")

# Loop through the range to find prime numbers
for number in range(start, end + 1):
    if number >= 2:
        prime = True
        # Check divisibility
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        # Print if prime
        if prime:
            print(number, end=" ")