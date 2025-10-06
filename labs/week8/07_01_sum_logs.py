"""
Log errors in the following function

"""


def add_em_up(*args):
    my_sum = 0
    for item in args:
        try:
            my_sum += item
        except TypeError:
            print(f"TypeError: Cannot add {item} of type {type(item)}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return my_sum


## Your logging should be able to report what went wrong with the follow code
print(add_em_up(1, 2, 3, 4))
print(add_em_up(1, 2, 3, "hi"))
print(add_em_up(1, 2, {3, 4}, "hi"))
print(add_em_up([1, 2, 3], [2, 3, 4], {3, 4}, "hi"))

