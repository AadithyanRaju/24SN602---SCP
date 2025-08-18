# convert the following code into a function
# your function should take a single list as input
# it should return a list with only the even numbers from the input list

def evenNumbers(inputList):
    return [i for i in inputList if i % 2 == 0]

numbers = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]
print(evenNumbers(numbers))

other_numbers = [213, 2, 3, 125, 12, 32, 21, 3, 6, 23, 12, 3, 326, 45, 12, 32, 14, 2]
print(evenNumbers(other_numbers))