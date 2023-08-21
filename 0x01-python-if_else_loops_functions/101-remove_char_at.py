#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ''

    for i in range(0, len(str)):
        if (i != n):
            str_cpy += str[i]
        else:
            continue

    return (str_cpy)
