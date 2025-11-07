import random

def play_game():
    # Available options for the game
    options = ['rock', 'paper', 'scissors']

    # 1- User input and standardization
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Input validation
    if user_choice not in options:
        print("Invalid input! Please choose 'rock', 'paper', or 'scissors'.")
        return  # End the function early

    # 2- computer's random choice
    computer_choice = random.choice(options)

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # 3- Determine the winner and display the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
play_game()
