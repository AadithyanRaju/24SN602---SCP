# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# you will need the `input()` function to collect information from the user

import getpass

lives = 5
count = 0
sets = set()
while lives and count<10:
    print(f"Lives : {lives}, Count: {count}")
    inputValue = getpass.getpass("Enter a number: ",)
    try:number = int(inputValue)
    except ValueError:
        print("Invalid input, please enter a number.")
        continue
    if number in sets:
        print("Duplicate input! You lose a point.")
        lives -= 1
    else:
        sets.add(number)
        count += 1
        print(f"Added to the set.")
if count >= 10:
    print("Congratulations! You created a set with more than 10 items.")
else:
    print("Game over! You lost all your lives.")
