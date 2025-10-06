"""
Write a function that accepts user input with the input() function
Try to convert their input to `int` and catch any exceptions that happen.

what kind of exceptions did you find?

"""

def get_int() -> int:
    user_input = input("Please enter an integer: ")
    try:
        return int(user_input)
    except ValueError:
        print("That's not a valid integer. Please try again.")
    except TypeError:
        print("Invalid type. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    result = get_int()
    if result is not None:
        print(f"You entered the integer: {result}")