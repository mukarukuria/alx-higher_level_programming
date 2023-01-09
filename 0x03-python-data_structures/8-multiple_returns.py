#!/usr/bin/python3
def multiple_returns(sentence):
    num = 1
    for i, let in enumerate(sentence):
        num = i + 1

    char = sentence[0]

    tuple_new = (num, char)

    return tuple_new
