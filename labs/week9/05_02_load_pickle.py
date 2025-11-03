"""
Load your pickled files from 05_01 and use them here!

"""
import pickle

class Car:
    cars_created = 0
    def __init__(self, num_tires = 2, color = "red", gas=True):
        self.num_tires = num_tires
        self.color = color
        self.gas = gas
    
    def is_gas(self):
        return self.gas

    def honk_horn(self):
        print("HONK HONK")
    
    def can_drive(self):
        if self.num_tires == 4:
            return True
        return False
    
with open('mycar', 'rb') as f:
    my_car = pickle.load(f)

print(my_car.num_tires)