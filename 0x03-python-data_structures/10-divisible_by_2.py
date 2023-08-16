#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for int in my_list:
        if int % 2:
            result.append(False)
        else:
            result.append(True)

    return result
