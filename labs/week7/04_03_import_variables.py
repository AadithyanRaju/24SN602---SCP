"""
Try importing not just your previous function, but also variables (from any previous file of your choice.)

"""
from a01_01_sum_ints_inf_args import sum_ints, sample_input

if __name__ == "__main__":
    print(sum_ints(*sample_input))