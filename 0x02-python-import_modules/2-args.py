#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    # Number of arguments without filename.
    argc = (len(argv) - 1)

    if argc == 1:
        print("{} argument:".format(argc))
    elif argc > 1:
        print("{} arguments:".format(argc))
    else:
        print("{} arguments.".format(argc))

    if argc >= 1:
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
