#!/usr/bin/python3
import sys
argv = sys.argv
argc = len(argv)

print("{:d} arguments".format(argc - 1), end="")

if argc == 1:
    print(".")
else:
    print(":")

for i in range(1, argc):
   print("{:d} {:s}".format(i, argv[i]))
