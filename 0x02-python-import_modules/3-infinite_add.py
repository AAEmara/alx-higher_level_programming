#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    sum_args = 0

    if argc > 1:
        for i in range(1, argc):
            sum_args += int(argv[i])

    print("{:d}".format(sum_args))
