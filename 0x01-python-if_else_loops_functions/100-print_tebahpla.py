#!/usr/bin/python3
i = 122
j = 0
while (i != 96):
    if (i % 2 == 1):
        j = 32
    else:
        j = 0

    print("{:c}".format(i - j), end="")
    i -= 1
