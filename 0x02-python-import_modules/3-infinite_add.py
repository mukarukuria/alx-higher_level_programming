#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    result = 0

    for i, arg in enumerate(argv):
        if i == 0:
            continue
        result += int(arg)

    print(f"{result}")
