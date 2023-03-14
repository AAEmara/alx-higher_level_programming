#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        frst_char = None
    else:
        frst_char = sentence[0][0]
    rtrn_tuple = len(sentence), frst_char
    return rtrn_tuple[0], rtrn_tuple[1]
