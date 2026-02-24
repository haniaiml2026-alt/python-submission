# Program 5: Bill Split Calculator
# This program calculates the total bill including tax and tip,
# and splits the final amount among a given number of people.

# Taking user input
total = float(input("Enter total bill amount: "))       # Original bill amount
people_count = int(input("Enter number of people: "))  # Number of people to split the bill
tax_rate = float(input("Enter tax percentage: "))      # Tax percentage
tip_rate = float(input("Enter tip percentage: "))      # Tip percentage

# Step 1: Store original amount
base_amount = total

# Step 2: Tax calculation
tax_amt = base_amount * tax_rate / 100                 # Calculating tax amount
new_amount = base_amount + tax_amt                     # Amount after adding tax

# Step 3: Tip calculation
tip_amt = new_amount * tip_rate / 100                 # Calculating tip amount
grand_total = new_amount + tip_amt                     # Total amount after tax and tip

# Step 4: Split bill among people
each_share = grand_total / people_count               # Amount each person pays

# Displaying results
print("\n----- BILL DETAILS -----")
print("Base amount:", round(base_amount, 2))
print("Tax amount:", round(tax_amt, 2))
print("Amount after tax:", round(new_amount, 2))
print("Tip amount:", round(tip_amt, 2))
print("Final total:", round(grand_total, 2))
print("Each person pays:", round(each_share, 2))