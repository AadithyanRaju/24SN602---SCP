# write a function that exits a for-loop with a return statement!


def find_first_divisible(list_of_nums, n):
    """
    input:
        list_of_nums: a list of numbers
        n: an integer

    Returns:
        The first number in the list that is divisble by n

    
    Example input: [1,2,3,4,5], 3
    output: 3
    
    """
    for num in list_of_nums:
        if num % n == 0:
            return num
    else:
        return None

    ## Use a for -loop to iterate over the input list
    ## check if the number is divisble by n with modulo
    ## if it is -- return the number immediately!
    ## This will exit the for-loop!!!

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_first_divisible(numbers, 3))
print(find_first_divisible(numbers, 10)) 