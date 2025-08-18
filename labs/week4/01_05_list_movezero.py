# Exercise

# Write a program to move all zero digits to end of a given list of numbers
# Expected output:
# Original list:

# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:

# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sample_list =  [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

x,y = 0,len(sample_list)-1

while sample_list[y]==0:
    y-=1

while x<y:
    if sample_list[x]==0:
        sample_list[x],sample_list[y]=sample_list[y],sample_list[x]
        y-=1
    x+=1
print(sample_list)