# Program 19: Text Analysis Functions
# This program analyzes a given text and provides information such as
# word count, vowels, consonants, reversed text, palindrome check,
# text without vowels, longest word, and word frequency.

# Function to count words
def count_words(text):
    return len(text.split())

# Function to count vowels
def count_vowels(text):
    return sum(1 for ch in text if ch.lower() in "aeiou")

# Function to count consonants
def count_consonants(text):
    return sum(1 for ch in text if ch.isalpha() and ch.lower() not in "aeiou")

# Function to reverse text
def reverse_text(text):
    return text[::-1]

# Function to check if text is a palindrome
def is_palindrome(text):
    t = text.replace(" ", "").lower()
    return t == t[::-1]

# Function to remove vowels from text
def remove_vowels(text):
    return "".join(ch for ch in text if ch.lower() not in "aeiou")

# Function to calculate word frequency
def word_frequency(text):
    freq = {}
    for w in text.lower().split():
        freq[w] = freq.get(w, 0) + 1
    return freq

# Function to find the longest word
def longest_word(text):
    return max(text.split(), key=len)

# Function to analyze text and display results
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    
    lw = longest_word(text)
    print(f"Longest word: {lw} ({len(lw)} letters)")
    
    print("Word Frequency:", end=" ")
    freq = word_frequency(text)
    print(", ".join(f"{w}: {c}" for w, c in freq.items()))

# Main program
text = input("Enter text: ")
analyze_text(text)