# Exercise

# Write a program to find the largest number in a list without using built-in functions

# [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
# output = 123123

# use a for loop
sample_list =  [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
max_num = sample_list[0]
for i in sample_list:
    if i>max_num:
        max_num = i
print(i)