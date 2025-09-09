"""
Create a class (you pick the name) that has
at least 5 methods.
3 of the methods must call other methods within them (using self.method name)
Run at least one method automatically in __init__ so it will run at start up

Demonstrate your methods work by creating an instance and running all the methods
"""
from random import randint
class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.introduce() 

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

    def play_game(self):
        print(f"{self.name} is playing a game.")
        self.__check_score()

    def __check_score(self):
        score = self.__calculate_score()
        print(f"{self.name}'s score is {score}.")

    def __calculate_score(self):
        return randint(0, 100)

    def celebrate_victory(self):
        print(f"{self.name} celebrates victory!" if self.score > 50 else f"{self.name} did not win this time.")

player = Player("AR75")
player.play_game()
player.celebrate_victory()
