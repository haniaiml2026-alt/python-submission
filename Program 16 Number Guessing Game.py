# Program 16: Number Guessing Game with Best Score and Hints
# This program allows the user to guess a randomly selected number 
# between 1 and 100. It provides hints, tracks attempts, and maintains 
# a best score (minimum attempts used).

import random

best_score = None  # Stores minimum attempts used across games

while True:
    # Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts_used = 0
    guessed_correctly = False

    # Display game instructions
    print("\nNUMBER GUESSING GAME")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    # Loop for user's attempts
    while attempts_used < max_attempts:
        guess = int(input("\nEnter your guess: "))
        attempts_used += 1
        attempts_left = max_attempts - attempts_used

        # Check if guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            print("Attempts used:", attempts_used)
            guessed_correctly = True

            # Update best score if applicable
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print("New Best Score!", best_score, "attempts")

            break

        # Give feedback if guess is too high or too low
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")

        # Bonus hint when guess is within 5 of the secret number
        if abs(guess - secret_number) <= 5:
            print("Hint: You are very close!")

        print("Attempts remaining:", attempts_left)

    # If user did not guess correctly
    if not guessed_correctly:
        print("\nGame Over! You used all attempts.")
        print("The correct number was:", secret_number)

    # Show best score so far
    if best_score is not None:
        print("Best score so far:", best_score, "attempts")

    # Ask user if they want to play again
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("Thanks for playing!")
        break