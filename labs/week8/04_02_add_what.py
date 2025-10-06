"""
Write a function that takes two inputs and attempts to add them together.

Use a try/except block to catch all possible errors

Try adding
int + int
int + str
str + list
tuple + list
dict + dict
dict + str

Are all the exceptions the same?
"""

def add_what(a, b):
    try:
        return a + b
    except TypeError as e:
        return f"TypeError: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
if __name__ == "__main__":
    print(add_what(1, 2))               
    print(add_what(1, 'hello'))         
    print(add_what('hello', [1, 2, 3])) 
    print(add_what((1, 2), [3, 4]))     
    print(add_what({'a': 1}, {'b': 2})) 
    print(add_what({'a': 1}, 'hello'))  