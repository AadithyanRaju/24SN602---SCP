# write a short command line game

# 1. ask the user for their name: (use the input() function)

# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their n ame begins with a consonant make an even better joke about it.

# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.

import random

random_number = random.randint(0, 10)

name = input("Please enter your name: ")
if name[0].lower() in 'aeiou':
    print(f"Aha! Your name {name} begins with a vowel!")
else:
    print(f"Ha! Your name {name} begins with a consonant!")

input_number = input("Pick a number between 1 and 10: ")
try:
    input_number = int(input_number)
except ValueError:
    print("Please enter a valid integer.")
    exit()
if input_number == random_number:
    print(f"Congratulations {name}, you guessed the right number: {random_number}!")
    

