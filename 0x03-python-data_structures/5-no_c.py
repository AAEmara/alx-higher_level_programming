#!/usr/bin/python3
def no_c(my_string):
    string_len = len(my_string)
    new_string = ''

    for i in range(0, string_len):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            new_string += my_string[i]
    return new_string
