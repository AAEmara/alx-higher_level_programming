#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = (len(argv) - 1)
    total = 0

    for i in range(1, argc + 1):
        total += int(argv[i])
    print(total)
