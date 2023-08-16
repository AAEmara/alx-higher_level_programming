#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    elif len(my_list) == 0:
        return None

    max_int = my_list[0]

    for int in my_list:
        if int > max_int:
            max_int = int

    return max_int
