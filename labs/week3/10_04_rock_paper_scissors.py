# write rock-paper-scissors game

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random

computer_choice = random.randint(1, 3)

# you can map each of rock / paper / scissors to an integer from 1 - 3

mapping = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

print("Welcome to Rock-Paper-Scissors!")
while True:
    [print(f"{key}: {value}") for key, value in mapping.items()]
    user_input = input("Please enter 1, 2, or 3: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue
    
    if user_input not in mapping:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue
    print(f"You chose {mapping[user_input]}.")
    print(f"Computer chose {mapping[computer_choice]}.")
    if user_input == computer_choice:
        print("It's a tie! Try again.")
    elif (user_input, computer_choice) in [(1, 3), (2, 1), (3, 2)]:
        print("You win!")
        break
    else:
        print("You lose! Try again.")
