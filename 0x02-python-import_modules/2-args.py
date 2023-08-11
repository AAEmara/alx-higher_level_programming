#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)

    print("{:d} argument".format(argc - 1), end="")

    if argc == 1:
        print("s.")
    elif argc == 2:
        print(":")
    else:
        print("s:")

    for i in range(1, argc):
        print("{:d}: {:s}".format(i, argv[i]))
