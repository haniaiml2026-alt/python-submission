# Program 11: Number Pattern Printer
# This program prints different number patterns based on user choice.
# The user selects a pattern type and the height (number of rows) of the pattern.

# Displaying pattern options
print("Choose pattern type:")
print("1 - Pattern 1")  # Increasing numbers per row
print("2 - Pattern 2")  # Repeating row number
print("3 - Pattern 3")  # Decreasing numbers per row
print("4 - Pattern 4")  # Pyramid-like increasing and decreasing numbers

# Taking user input
choice = int(input("Enter pattern number: "))
n = int(input("Enter height: "))

print()

# Pattern 1: Increasing numbers per row
if choice == 1:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# Pattern 2: Repeating row number
elif choice == 2:
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

# Pattern 3: Decreasing numbers per row
elif choice == 3:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Pattern 4: Pyramid-like pattern (increasing then decreasing numbers)
elif choice == 4:
    for i in range(1, n+1):
        # increasing numbers
        for j in range(1, i+1):
            print(j, end="")
        # decreasing numbers
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()

# Invalid choice handling
else:
    print("Invalid pattern choice")