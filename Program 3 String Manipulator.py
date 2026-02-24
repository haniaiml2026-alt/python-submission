# Program 3: String Manipulator
# This program takes a sentence from the user and performs various 
# operations like counting characters and words, changing case, 
# finding first and last word, and reversing the sentence.

# Taking sentence input from the user
sentence = input("Enter a sentence: ")

# Storing the original sentence
original = sentence

# Counting characters
char_with_spaces = len(sentence)                       # Total characters including spaces
char_without_spaces = len(sentence.replace(" ", ""))  # Total characters excluding spaces

# Counting words
words = sentence.split()       # Split sentence into words
total_words = len(words)       # Count total words

# Case conversions
upper_case = sentence.upper()  # Convert sentence to uppercase
lower_case = sentence.lower()  # Convert sentence to lowercase
title_case = sentence.title()  # Convert sentence to title case (first letter of each word capitalized)

# Finding first and last word
first_word = words[0]          # First word of the sentence
last_word = words[-1]          # Last word of the sentence

# Reversing the sentence
reversed_sentence = sentence[::-1]  # Reverse the entire sentence

# Displaying results
print("\nResults:")
print("Original:", original)
print("Characters (with spaces):", char_with_spaces)
print("Characters (without spaces):", char_without_spaces)
print("Words:", total_words)
print("UPPERCASE:", upper_case)
print("lowercase:", lower_case)
print("Title Case:", title_case)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_sentence)