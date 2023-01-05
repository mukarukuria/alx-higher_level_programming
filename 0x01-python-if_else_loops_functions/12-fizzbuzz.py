#!/usr/bin/python3


def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz", end=" ")
            continue
        elif num % 5 == 0:
            print("Buzz", end=" ")
            continue
        elif num % 3 == 0:
            print("Fizz", end=" ")
            continue
        else:
            print(num, end=" ")
