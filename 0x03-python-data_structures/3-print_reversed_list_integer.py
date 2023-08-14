#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    max_idx = -len(my_list)
    i = -1

    while i >= max_idx:
        print("{:d}".format(my_list[i]))
        i -= 1
