#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)

    for name in names:
        if name[0] == "_" and name[1] == "_":
            continue
        print("{:s}".format(name))
