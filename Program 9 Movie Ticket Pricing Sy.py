# Program 9: Movie Ticket Pricing System
# This program calculates the total cost of movie tickets based on
# age, number of tickets, day of the week, and applicable discounts.

# Taking input from user
age = int(input("Enter age: "))                # Age of the customer
day = input("Enter day of week: ")            # Day of the week
tickets = int(input("Enter number of tickets: "))  # Number of tickets

# Decide base ticket price based on age
if age < 3:
    price = 0
    category = "Free"
elif age <= 12:
    price = 150
    category = "Child"
elif age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

# Calculate base total
base_total = price * tickets

# Check for discount on weekend (Friday, Saturday, Sunday)
if day.lower() in ["friday", "saturday", "sunday"]:
    discount = base_total * 0.20    # 20% discount
else:
    discount = 0

# Final amount after discount
final_total = base_total - discount

# Displaying ticket details
print("\n--- TICKET DETAILS ---")
print("Category:", category)
print("Price per ticket: ₹", price)
print("Base amount: ₹", base_total)
print("Discount: ₹", discount)
print("Amount after discount: ₹", final_total)
print("Total tickets:", tickets)
print("Total to pay: ₹", final_total)