"""
Write 3 classes which are related to each other
1) a monster class
2) a night-monster class (they only come out at night)
3) a full moon monster class (they only come out at night and on the full moon)

Make use of inheritance to save your code!

## Monster class
# class attribute
time_of_day (will need to activate night monsters)
day_of_month
full_moon (boolean)

# attributes
name
number of limbs
attack mode (magic, physical, mental hypnosis etc)
scare factor
weakness
life points

# methods
basic attack (attack something)
sleep (get life points back)
defend (something attacks it!)

## Night monster
same as above, but also special powers that activate at night
vulnerable in daylight


## full moon monster
only active in the full moon
"""
from random import randint
from typing import override
from concurrent import futures
import threading
import time


class Monster:
    time_of_day = 0
    day_of_month = 0
    full_moon = False

    def __init__(self, name:str, limbs:int, attack_mode:str, scare_factor:int, weakness:str, life_points:int):
        self.name = name
        self.limbs = limbs
        self.attack_mode = attack_mode # magic, physical, mental hypnosis etc
        self.scare_factor = scare_factor
        self.weakness = weakness
        self.life_points = life_points
        self.sleep = False

    def basic_attack(self, target):
        target.defend(self.attack_mode)

    def sleep(self):
        self.sleep = True
        self.life_points += randint(1,30)

    def awake(self):
        self.sleep = False

    def defend(self, attack):
        if attack == "magic":
            self.life_points -= 10
        elif attack == "physical":
            self.life_points -= 5
        elif attack == "mental hypnosis":
            self.life_points -= 15 * self.scare_factor

    def checkActive(self):
        return True

class NightMonster(Monster):
    def __init__(self, name:str, limbs:int, attack_mode:str, scare_factor:int, weakness:str, life_points:int):
        super().__init__(name, limbs, attack_mode, scare_factor, weakness, life_points)

    @override
    def checkActive(self):
        return True if Monster.time_of_day in [*[x for x in range(0,6)],*[x for x in range(18,24)]] else False

    def special_power(self):
        pass

class FullMoonMonster(NightMonster):
    def __init__(self, name:str, limbs:int, attack_mode:str, scare_factor:int, weakness:str, life_points:int):
        super().__init__(name, limbs, attack_mode, scare_factor, weakness, life_points)
    
    @override
    def checkActive(self):
        return super().checkActive() and Monster.full_moon

    def special_power(self):
        pass
        
class Human:
    def __init__(self, name: str, age: int, profession: str, life_points: int = 100):
        self.name = name
        self.age = age
        self.profession = profession
        self.life_points = life_points

    def speak(self):
        print(f"Hello, my name is {self.name}.")

    def work(self):
        print(f"I am working as a {self.profession}.")

    def defend(self, attack):
        if attack == "magic":
            self.life_points -= 8
        elif attack == "physical":
            self.life_points -= 12
        elif attack == "mental hypnosis":
            self.life_points -= 20

    def is_alive(self):
        return self.life_points > 0
    