#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    if my_list is None:
        return None

    for int in my_list:
        if int > max_int:
            max_int = int

    return max_int
