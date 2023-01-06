#!/usr/bin/python3
from sys import argv
result = 0

for i, arg in enumerate(argv):
    if i == 0:
        continue
    result += int(arg)

print(f"{result}")
