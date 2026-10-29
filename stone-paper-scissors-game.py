
# Import random so the computer can choose randomly
import random

# Store all the possible choices in a list
choices = ["stone", "paper", "scissor"]

# Ask the user to enter a choice
user = input("Enter stone, paper, or scissor: ").lower()

# Check whether the user's choice is valid
if user not in choices:
    print("Invalid choice! Please try again.")

else:
    # Let the computer select one choice randomly
    computer = random.choice(choices)

    # Display both choices
    print("Your choice:", user)
    print("Computer's choice:", computer)

    # If both choices are the same, it is a draw
    if user == computer:
        print("It's a draw!")

    # Check the three situations where the user wins
    elif (user == "stone" and computer == "scissor") or \
         (user == "scissor" and computer == "paper") or \
         (user == "paper" and computer == "stone"):
        print("You win!")

    # If neither a draw nor a user win, the computer wins
    else:
        print("Computer wins!")
