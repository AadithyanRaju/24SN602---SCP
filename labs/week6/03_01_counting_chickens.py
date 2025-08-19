"""
create a chicken class that has the following

# class attributes
time_of_day
number_of_eggs_laid

# instance attributes (uses the self variable)
breed
gender
weight
lays_eggs (boolean)

# methods
lay_egg --> this function should depend on time of day (chickens only lay eggs at night!),
it should also use random numbers to deterimine if laying the egg worked or not


## Create 100 instances of your chickens using a for loop

Use a for loop to update the time of day (go through each hour of the day)
within the loop have your chickens all try to lay eggs
Afterwards, print out how many total eggs were hatched -- for all chickens and individually.
What was the average number of eggs per chicken?
"""
from random import randint
class Chicken:
    time_of_day = 601
    number_of_eggs_laid = 0

    def __init__(self, breed:str = "Rooster", gender:str = "female", weight:float = 12.0, lays_eggs:bool = True):
        self.breed = breed
        self.gender = gender
        self.weight = weight
        self.lays_eggs = False if gender.lower == "male" else lays_eggs
        self.laid_eggs = 0

    def lay_egg(self,time_of_day:int = 1000):
        if time_of_day > 600 and time_of_day < 2000 :
            return    
        flag = 1 if randint(0,1) else 0
        self.number_of_eggs_laid += flag
        self.laid_eggs += flag

chickens = []
for i in range(100):
    chickens.append(Chicken())

for hour in range(24):
    Chicken.time_of_day = hour*100
    for chicken in chickens:
        chicken.lay_egg(Chicken.time_of_day)

total_eggs = 0
for chicken in chickens:
    total_eggs += chicken.laid_eggs
    print(f"{chicken.breed} laid {chicken.laid_eggs} eggs.")
print(f"Total eggs laid by all chickens: {total_eggs}")
average_eggs = total_eggs / len(chickens)
print(f"Average eggs per chicken: {average_eggs:.2f}")