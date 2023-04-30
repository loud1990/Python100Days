# Higher or Lower Game
# Instructions
# You will get two options of celebrities, and you have to guess which one has more followers on Instagram.

from art import logo, vs
import random
import os
from game_data import data

# Keep track of the score.
score = 0

# Format the game so that it asks the user if they want to play again at the end of the game.


def play_again():
    again = input("Do you want to play again? Type 'y' or 'n': ")
    if again == 'y':
        return True
    else:
        return False

# Compare A: random account from the game data vs Compare B: random account from the game data.
# Generate a random account from the game data.


def random_account():
    return random.choice(data)


def play_game():
    # Clear the screen
    os.system('cls')

    # Print the logo.
    print(logo)

    # Keep track of the score.
    global score
    account_A = random_account()
    account_B = random_account()
    # Make sure account A and B are not the same.
    while account_A == account_B:
        account_B = random_account()
    print(f"Compare A: {account_A['name']}, a {account_A['description']}, from {account_A['country']}.")
    print(vs)
    print(f"Against B: {account_B['name']}, a {account_B['description']}, from {account_B['country']}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    correct_guess = False

    # Check if user is correct.
    if guess == 'a':
        if account_A['follower_count'] > account_B['follower_count']:
            correct_guess = True
        else:
            correct_guess = False
    else:
        if account_B['follower_count'] > account_A['follower_count']:
            correct_guess = True
        else:
            correct_guess = False

    if correct_guess:
        print("You're right!")
        score += 1
        print(f"Current score: {score}")
    else:
        print("You're wrong!")
        print(f"Final score: {score}")
        score = 0
    if play_again():
        os.system('cls')
        play_game()
    else:
        print(f"Final score: {score}")
        score = 0
        print("Goodbye!")
        return
# Get user input for which is bigger.
# Get follower count of each account.
# Use if statement to check if user is correct.
# Clear the screen between rounds.
# Make the game repeatable.
# Don't forget to import clear and art only once you're done.


play_game()
