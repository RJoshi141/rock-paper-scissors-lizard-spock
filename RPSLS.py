import random

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors/lizard/spock): ")
    while choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
        choice = input("Invalid input. Please enter your choice again (rock/paper/scissors/lizard/spock): ")
    return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "rock":
        if computer_choice in ["scissors", "lizard"]:
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "paper":
        if computer_choice in ["rock", "spock"]:
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "scissors":
        if computer_choice in ["paper", "lizard"]:
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "lizard":
        if computer_choice in ["paper", "spock"]:
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "spock":
        if computer_choice in ["rock", "scissors"]:
            return "You win!"
        else:
            return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

play_game()
