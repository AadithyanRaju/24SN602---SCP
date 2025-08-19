"""
create a simple bicylce class

# Attributes
number of tires
type of of tires (road vs mountain bike)
model
color
number of speeds
brakes (front or back or both)
current speed.

# Methods
brake
pedal faster (should affect speed)
"""

class Bicycle:
    def __init__(self, model:str, color:str, number_of_speeds:int,number_of_tyres:int = 2, tire_type:str = "road", breaks:str = "both"):
        self.number_of_tires = number_of_tyres
        self.tire_type = tire_type
        self.model = model
        self.color = color
        self.number_of_speeds = number_of_speeds
        self.brakes = breaks
        self.current_speed = 0

    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 1

    def pedal_faster(self):
        self.current_speed += 1