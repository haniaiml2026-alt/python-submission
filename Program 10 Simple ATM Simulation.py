# Program 10: Simple ATM Simulation
# This program simulates a basic ATM allowing the user to
# check balance, deposit money, withdraw money, and exit.

# Starting balance
balance = 10000   # Initial account balance in ₹

while True:
    # Displaying ATM menu
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Taking user choice
    choice = int(input("Enter choice: "))

    # Option 1: Check balance
    if choice == 1:
        print("Current balance: ₹" + str(balance))

    # Option 2: Deposit money
    elif choice == 2:
        deposit_amt = float(input("Enter amount to deposit: ₹"))
        if deposit_amt > 0:
            balance = balance + deposit_amt
            print("Deposit successful!")
            print("New balance: ₹" + str(balance))
        else:
            print("Invalid deposit amount.")

    # Option 3: Withdraw money
    elif choice == 3:
        withdraw_amt = float(input("Enter amount to withdraw: ₹"))
        
        # Check minimum balance rule
        if withdraw_amt > balance:
            print("Insufficient balance.")
        elif balance - withdraw_amt < 500:
            print("Cannot withdraw. Minimum balance of ₹500 must remain.")
        else:
            balance = balance - withdraw_amt
            print("Withdrawal successful!")
            print("New balance: ₹" + str(balance))

    # Option 4: Exit
    elif choice == 4:
        print("Thank you for using ATM.")
        break

    # Invalid choice
    else:
        print("Invalid choice. Try again.")