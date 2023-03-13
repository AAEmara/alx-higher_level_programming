#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1 or len(tuple_b) < 1:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        if len(tuple_b) == 0:
            tuple_b = 0, 0

    elif len(tuple_a) == 1 or len(tuple_b) == 1:
        if len(tuple_a) == 1:
            tuple_a = tuple_a[0], 0
        if len(tuple_b) == 1:
            tuple_b = tuple_a[0], 0

    else:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]

    frst_element = tuple_a[0] + tuple_b[0]
    scnd_element = tuple_a[1] + tuple_b[1]

    return (frst_element, scnd_element)
