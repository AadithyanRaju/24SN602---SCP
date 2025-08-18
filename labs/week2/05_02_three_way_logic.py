# 1) Initialize variable a to true, b to false and c to true
a = True
b = False
c = True
print(f'a = {a}, b = {b}, c = {c}')
# 2) If you print(a and b or c) what it will return? Why?
# Does the order of operations matter?
print(f'a and b or c = {a and b or c}')

# 3) Is print(a or b and c) different?
print(f'a or b and c = {a or b and c}')

# 4)Assign c to false and print the value of a and b or c
c = False
print(f'a = {a}, b = {b}, c = {c}, a and b or c = {a and b or c}')

# Understand the difference in each scenario
# What is happening here?


# 5) Now try to use some ()'s to force python to evaluate it differently.

a= False
c= True

print(f'a = {a}, b = {b}, c = {c}')
print(f'(a and b) or c = {(a and b) or c}')
print(f'a and (b or c) = {a and (b or c)}')

