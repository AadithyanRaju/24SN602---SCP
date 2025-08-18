# Exercise

# Use a for-loop to find the sum of numbers from 1 to 100
# you will need the range() function.

#print(f"Sum of numbers from 1 to 100 is: {sum(range(1, 101))}")
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of numbers from 1 to 100 is: {total}")