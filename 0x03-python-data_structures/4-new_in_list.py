#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None

    list_cpy = my_list.copy()
    max_id = len(my_list) - 1

    if idx < 0:
        return my_list
    elif idx > max_id:
        return my_list
    else:
        list_cpy[idx] = element
        return list_cpy
