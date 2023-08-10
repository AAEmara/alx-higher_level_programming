#!/usr/bin/python3
def uppercase(str):

    for char in str:
        if ord(char) in range(97, 97 + 26):
            char = chr(ord(char) - 32)

        print("{:s}".format(chr(ord(char))), end="")

    print()
