# Program 13: Sum and Average Calculator
# This program calculates the sum, average, maximum, and minimum
# of a set of numbers entered by the user.

# Ask how many numbers the user wants to enter
count = int(input("How many numbers? "))

# Initialize variables
total = 0            # To store sum of numbers
largest = None       # To track the largest number
smallest = None      # To track the smallest number

# Loop to take numbers from the user
for i in range(1, count + 1):
    value = float(input("Enter number " + str(i) + ": "))
    
    # Add to total
    total += value
    
    # Set first value as initial max and min, then update
    if largest is None or value > largest:
        largest = value
        
    if smallest is None or value < smallest:
        smallest = value

# Calculate average
avg = total / count

# Display results
print("\nResults:")
print("Sum:", total)
print("Average:", avg)
print("Maximum:", largest)
print("Minimum:", smallest)