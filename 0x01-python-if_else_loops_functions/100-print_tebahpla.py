#!/usr/bin/python3

for ch in range(ord('z'), ord('a') - 1, -1):
    if ch % 2 == 0:
        print("{}".format(chr(ch)), end="")
    else:
        print(chr(ch - 32), end="")
