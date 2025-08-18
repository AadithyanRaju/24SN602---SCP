#Exercise

#Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

n = input("Please enter the number: ")
try:
    n = int(n)
except ValueError:
    print("Please enter a valid integer.")
    exit()

for i in range(1, n + 1):
    print('* ' * i)
for i in range(n - 1, 0, -1):
    print('* ' * i)