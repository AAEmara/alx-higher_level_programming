#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{:d}".format(i))
    else:
        print("{:0>2d}, ".format(i), end="")
