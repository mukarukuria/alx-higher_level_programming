#!/usr/bin/python3
def multiple_returns(sentence):
    num = 1
    tuple_new = ()
    if sentence == "":
        tuple_new = (0, None)
        return tuple_new

    for i, let in enumerate(sentence):
        num = i + 1

    char = sentence[0]

    tuple_new = (num, char)

    return tuple_new
