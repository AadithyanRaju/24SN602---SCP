# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

import sys
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.has_sword = False
        self.has_seen_sword = False

    def pick_up_sword(self):
        self.has_sword = True
        print(f"{self.name} has picked up the sword!")

    def fight_dragon(self):
        if self.has_sword:
            print(f"{self.name} bravely fights the dragon and wins!")
            sys.exit("Congratulations! You have defeated the dragon and won the game!")
        else:
            print(f"{self.name} tries to fight the dragon but is eaten!")
            sys.exit("Game Over! You were eaten by the dragon.")

def print_room(x,y, dragon=False, dragon_coodinates=(1, 2) ,sword=False, sword_coordinates=(1, 4)):
    print("_______")
    for i in range(5):
        print("|", end="")
        for j in range(5):
            if dragon and (i, j) == dragon_coodinates:
                print("D", end="")
            elif sword and (i, j) == sword_coordinates:
                print("S", end="")
            elif i == x and j == y:
                print("P", end="")
            else:
                print(" ", end="")
        print("|")
    print("--| |--")

def empty_room(player):
    print(f"You are in a empty room{" with a sword" if player.has_seen_sword and not player.has_sword else ""}!")
    print_room(4, 2,  sword=(True if player.has_seen_sword and not player.has_sword else False))
    print(f"Options:\n1. {("Look around\n2." if not player.has_seen_sword else "Pick up the sword.\n2.") if not player.has_sword else""} Return to the main room")
    choice = input("Choose an option (1/2): ").strip()
    if choice == '1':
        if player.has_sword:
            main_room(player)
        if not player.has_seen_sword:
            print("You look around the room and find a sword!")
            player.has_seen_sword = True
            empty_room(player)
        if not player.has_sword:
            player.pick_up_sword()
    elif choice == '2':
        if player.has_seen_sword and not player.has_sword:
            print("You have left the sword behind.")
        main_room(player)
    else:
        print("Invalid choice. ")
    pause = input("Press Enter to continue...")
    empty_room(player)
    

def dragon_room(player):
    print("You have entered the dragon's lair!")
    print_room(4, 2, dragon=True)
    print("Options:\n1. Fight the dragon\n2. Return to the main room")
    choice = input("Choose an option (1/2): ").strip()
    
    if choice == '1':
        player.fight_dragon()
    elif choice == '2':
        main_room(player)
    else:
        print("Invalid choice. ")
    
    pause = input("Press Enter to continue...")

def main_room(player):
    print("You are in a large room with two doors.")
    choice = input("Do you want to go through the left door or the right door? (left/right): ").strip().lower()
    
    if choice in ["left", 'l']:
        empty_room(player)
    elif choice in ["right", 'r']:
        dragon_room(player)
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        main_room()


name = input("Enter your name: ")
print(f"Welcome to the CLI RPG, {name}!")
print("You find yourself in a mysterious world.")
player = Player(name)
main_room(player)