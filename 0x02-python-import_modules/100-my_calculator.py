#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    argc = len(argv)

    if argc != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
