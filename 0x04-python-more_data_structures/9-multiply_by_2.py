#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i, el in enumerate(a_dictionary):
        new_dictionary[el] = a_dictionary[el] * 2

    return new_dictionary
