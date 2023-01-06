#!/usr/bin/python3
from sys import argv
arguments = len(argv) - 1

if arguments == 0:
    print("{} arguments.".format(arguments))
#    break
elif arguments == 1:
    print("{} argument:".format(arguments))
else:
    print("{} arguments:".format(arguments))

for i, arg in enumerate(argv):
    if i == 0:
        continue
    print("{}: {}".format(i, arg))
