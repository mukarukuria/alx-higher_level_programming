#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, stdout, exit

if len(argv) - 1 != 3:
    stdout.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
    exit(1)

a = int(argv[1])
b = int(argv[3])

if argv[2] == '+':
    stdout.write(f"{a} + {b} = {add(a, b)}\n")
    exit(0)
elif argv[2] == '-':
    stdout.write(f"{a} - {b} = {sub(a, b)}\n")
    exit(0)
elif argv[2] == '*':
    stdout.write(f"{a} * {b} = {mul(a, b)}\n")
    exit(0)
elif argv[2] == '/':
    stdout.write(f"{a} / {b} = {div(a, b)}\n")
    exit(0)
else:
    stdout.write("Unknown operator. Available operators: +, -, * and /\n")
    exit(1)