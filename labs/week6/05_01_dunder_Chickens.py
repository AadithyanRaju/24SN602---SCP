"""
Update your chicken class to include the following dunders

__str__  : make some nice str format for your chicken. 
When we print your chicken it should tell us: how heavy the chicken is, the gender and how many eggs it has laid (if has)

__add__ : what happens when you add two chickens together? If they are male and female, create a baby chicken! (a new chicken) Otherwise, nothing?

"""
from random import randint
class Chicken:
    time_of_day = 601
    number_of_eggs_laid = 0
    chickens = []

    def __init__(self, breed:str = "Rooster", gender:str = "female", weight:float = 12.0, lays_eggs:bool = True):
        self.breed = breed
        self.gender = gender
        self.weight = weight
        self.lays_eggs = False if gender.lower == "male" else lays_eggs
        self.laid_eggs = 0
        Chicken.chickens.append(self)

    def lay_egg(self,time_of_day:int = 1000):
        if time_of_day > 600 and time_of_day < 2000 :
            return    
        flag = 1 if randint(0,1) else 0
        self.number_of_eggs_laid += flag
        self.laid_eggs += flag
    
    def __str__(self):
        return f"This Chicken is a {self.breed} weighing {self.weight} kg, is {self.gender} and has laid {self.laid_eggs} eggs."
    
    def __add__(self, other):
        if isinstance(other, Chicken):
            gen = set([self.gender.lower,other.gender.lower])
            if len(gen) == 2:
                gender = "female" if randint(0,1) else "male"
                laysEgg = True if gender == "female" else False
                newChick = Chicken(breed=self.breed,gender=gender,weight=0.5,lays_eggs=laysEgg)
                Chicken.chickens.append(newChick)
                return newChick
    
