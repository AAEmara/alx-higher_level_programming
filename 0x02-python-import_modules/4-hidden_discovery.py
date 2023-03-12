#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in range(len(names)):
        if "__" in names[i][:2]:
            continue
        else:
            print(names[i])
