#!/usr/bin/python3

"""1-my_list module that contains MyList class"""


class MyList(list):
    """MyList class.
    """
    def print_sorted(self):
        print(sorted(self))
