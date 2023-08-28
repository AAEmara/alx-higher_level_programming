#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))

    except ValueError:
        print("Input is not an integer value.")

    except TypeError:
        print("Please check the datatype entered.")

    else:
        return (True)

    return (False)
