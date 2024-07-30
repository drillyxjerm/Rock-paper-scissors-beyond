import random

def rock_paper_scissors_lizard_spock():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    win_conditions = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    computer_choice = random.choice(choices)

    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    player_choice = input("Enter your choice: ").lower()

    if player_choice not in choices:
        print("Invalid choice. Please choose from rock, paper, scissors, lizard, or spock.")
        return

    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif computer_choice in win_conditions[player_choice]:
        print("You win!")
    elif player_choice in win_conditions[computer_choice]:
        print("You lose!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    rock_paper_scissors_lizard_spock()
