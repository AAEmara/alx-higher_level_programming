#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        list_cpy = my_list.copy()
        list_cpy = list_cpy[: x]
        count = 0

    except AttributeError:
        print("Please enter a list.")
        return (count)

    except TypeError:
        print("Please check the number of values entered to print.")
        return (count)

    for i in range(0, x):
        try:
            print("{:d}".format(list_cpy[i]), end='')

        except (ValueError, TypeError):
            pass

        else:
            count += 1

    print()
    return(count)
