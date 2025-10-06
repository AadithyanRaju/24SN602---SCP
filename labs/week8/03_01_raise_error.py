"""
Write a function that accepts user input with the input() function
Specify that they must use alphabet characters only.
Then raise an exception if they enter anything that is not able an alphabet character!

Hint: you can use .isalpha() to check if a character is an alpha character.
"""

def readInput():
    user_input = input("Enter alphabet characters only: ")
    if not user_input.isalpha():
        raise ValueError("Input must contain alphabet characters only.")
    return user_input

if __name__ == "__main__":
    try:
        result = readInput()
        print(f"You entered: {result}")
    except ValueError as e:
        print(f"Error: {e}")