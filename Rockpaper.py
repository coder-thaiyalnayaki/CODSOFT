import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"Result: {result}")

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n===== Rock, Paper, Scissors Game =====")
        print("Choose: 1. Rock, 2. Paper, 3. Scissors, 4. Quit")

        user_input = input("Enter your choice (1-4): ")

        if user_input == "4":
            print("\nExiting the game. Thanks for playing!")
            break
        elif user_input not in ["1", "2", "3"]:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            continue

        user_choice = ""
        if user_input == "1":
            user_choice = "rock"
        elif user_input == "2":
            user_choice = "paper"
        elif user_input == "3":
            user_choice = "scissors"

        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissors_game()
