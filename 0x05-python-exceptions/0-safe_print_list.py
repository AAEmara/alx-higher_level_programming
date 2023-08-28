#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        list_cpy = my_list.copy()
        list_cpy = list_cpy[: x]

    except AttributeError:
        print("Please enter a list in the first argument.")

    except TypeError:
        print("Please check the datatype entered.")

    else:
        i = 0

        for element in list_cpy:
            print("{}".format(element), end='')
            i += 1

        print()
        return (i)

    return (0)
