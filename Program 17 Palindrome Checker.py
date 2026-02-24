# Program 17: Palindrome Checker
# This program checks whether a given word or number is a palindrome.
# It displays the original and reversed values and compares them.

# Taking input from user
user_input = input("Enter word/number: ")

# Store original value
original = user_input

# Reverse the input using a loop (without using built-in reverse)
reversed_text = ""
for ch in user_input:
    reversed_text = ch + reversed_text

# Display original and reversed values
print("Original:", original)
print("Reversed:", reversed_text)

# Compare ignoring case to determine if palindrome
if original.lower() == reversed_text.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")