# Program 7: Menu-Driven Temperature Conversion
# This program allows the user to convert temperatures between
# Celsius, Fahrenheit, and Kelvin using a menu-driven approach.
# The user can repeatedly choose conversion options until they exit.

while True:
    # Displaying the conversion menu
    print("\n--- Temperature Conversion Menu ---")
    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")
    print("3 - Celsius to Kelvin")
    print("4 - Kelvin to Celsius")
    print("5 - Fahrenheit to Kelvin")
    print("6 - Kelvin to Fahrenheit")
    print("7 - Exit")

    # Taking user choice
    option = int(input("Choose an option: "))

    # Celsius to Fahrenheit
    if option == 1:
        cel = float(input("Enter Celsius value: "))
        result = (cel * 9/5) + 32
        print("Converted value:", round(result, 2), "F")

    # Fahrenheit to Celsius
    elif option == 2:
        fah = float(input("Enter Fahrenheit value: "))
        result = (fah - 32) * 5/9
        print("Converted value:", round(result, 2), "C")

    # Celsius to Kelvin
    elif option == 3:
        cel = float(input("Enter Celsius value: "))
        result = cel + 273.15
        print("Converted value:", round(result, 2), "K")

    # Kelvin to Celsius
    elif option == 4:
        kel = float(input("Enter Kelvin value: "))
        result = kel - 273.15
        print("Converted value:", round(result, 2), "C")

    # Fahrenheit to Kelvin
    elif option == 5:
        fah = float(input("Enter Fahrenheit value: "))
        result = (fah - 32) * 5/9 + 273.15
        print("Converted value:", round(result, 2), "K")

    # Kelvin to Fahrenheit
    elif option == 6:
        kel = float(input("Enter Kelvin value: "))
        result = (kel - 273.15) * 9/5 + 32
        print("Converted value:", round(result, 2), "F")

    # Exit option
    elif option == 7:
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid input. Please select a number between 1 and 7.")