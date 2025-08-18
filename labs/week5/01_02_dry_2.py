# rewrite your function from the previous exercise (01_01_dry.py)
# this time your function should be able change the divisible by number.

# I should be able to return the list of numbers which is divisible by "n", where
# 'n' can be any number.

## Input: a list of integers, a number 'n'
## output: a new list that only has retains numbers which are divisible by n

def divisibleNumbers(inputList, n):
    return [i for i in inputList if i % n == 0]

numbers = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]
print(divisibleNumbers(numbers, 2))
print(divisibleNumbers(numbers, 3))