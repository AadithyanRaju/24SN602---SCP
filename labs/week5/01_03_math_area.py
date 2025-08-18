# write a function that takes the length and width of a rectangle and returns the area


# write another function that finds the area of a cube
# bonus challenge: use your first function inside this function!


# write a function that finds the area of a sphere
# hint: you can get `pi` by importing math (google it!)

from math import pi

def rectangleArea(length, width):
    return length * width
def cubeArea(side_length):
    return rectangleArea(side_length, side_length) * 6 
def sphereArea(radius):
    return 4 * pi * (radius ** 2)

print("Area of rectangle (length=5, width=3):", rectangleArea(5, 3))
print("Area of cube (side_length=4):", cubeArea(4)) 
print("Area of sphere (radius=2):", sphereArea(2))
