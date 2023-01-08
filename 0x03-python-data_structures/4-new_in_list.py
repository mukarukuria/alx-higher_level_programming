#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []

    if idx < 0 or idx > len(my_list):
        return None

    new_list = []

    for i, el in enumerate(my_list):
        if i == idx:
            new_list.append(element)
            continue
        new_list.append(el)

    return new_list
