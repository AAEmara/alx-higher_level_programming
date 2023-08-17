#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        max_val = None
        max_val_key = None
    else:
        max_val = -1
        for key, vlaue in a_dictionary.items():
            if a_dictionary[key] > max_val:
                max_val = a_dictionary[key]
                max_val_key = key

    return max_val_key
