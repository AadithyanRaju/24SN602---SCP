"""
Use JSON to serialize the following dictionary

"""
import json

my_dict = {i: i ** 2 for i in range(10_000)}

with open('w9.json', 'w') as f:
    json.dump(my_dict, f)
    f.close()

# after creating your JSON file, try opening it the file by double clicking it in the explorer
# can you read it ? Why or why not?

# use code to load your json file into a new variable
# print it out to make sure it's the same.

with open('w9.json','r') as f:
    new_dict = json.load(f)
    f.close()

print(new_dict)