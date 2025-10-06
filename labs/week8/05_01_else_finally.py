"""
implement a key-lookup procedure for a dictionary

Try to get the key and update the value by n
If an en exception is raised, handle it by creating the key with a default value
if no exception is raised, update the value
Regardless of what happens, print the dictionary
"""

def update_dict(my_dict: dict, key: str, n: int, default: int) -> None:
    try:
        my_dict[key] += n
    except KeyError:
        my_dict[key] = default
    finally:
        print(my_dict)

if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2}
    update_dict(my_dict, 'a', 3, 10)  
    update_dict(my_dict, 'c', 3, 10)  