# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it
#------------------------------------------------------------------------

import random

# Choose a Word form English Dict
with open('dictionary.txt', 'r') as fp:randomWord = random.choice(fp.readlines())[:-1];fp.close()

# ____ for user view
userView = '_ '*len(randomWord)

counter = 0
guessSet = set()
print("Welcome to Hangman! Try to guess the word, one letter at a time.")
while counter < 6:
    print(f'Word: {userView}\nTries left: {6 - counter}')
    guess = input('Enter your guess (a single letter): ').upper()
    if guess in guessSet:
        print("You've already guessed that letter.")
        continue
    guessSet.add(guess)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single alphabetic character.")
        continue
    
    if guess in randomWord:
        print(f"Good guess! '{guess}' is in the word.")
        userView = ' '.join([char if char == guess or userView.split()[i] != '_' else '_' for i, char in enumerate(randomWord)])
        
        if '_' not in userView:
            print(f"Congratulations! You've guessed the word: {randomWord.strip()}")
            break
    else:
        counter += 1
        print(f"Sorry, '{guess}' is not in the word.")
else:
    print(f"Game over! The word was: {randomWord.strip()}")
