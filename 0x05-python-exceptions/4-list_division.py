#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        list_1 = my_list_1.copy()
        list_2 = my_list_2.copy()
        new_list = []

    except TypeError:
        print("Please check the number of elements entered.")
    except AttributeError:
        print("Please enter a list for the first or second argument.")

    finally:
        for i in range(0, list_length):
            try:
                new_list.append(list_1[i] / list_2[i])

            except TypeError:
                new_list.append(0)
                print("wrong type")

            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")

            except IndexError:
                new_list.append(0)
                print("out of range")

    return (new_list)
