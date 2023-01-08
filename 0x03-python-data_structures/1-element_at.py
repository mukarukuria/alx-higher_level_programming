#!/usr/bin/python3
def element_at(my_list, idx):
    result = 0
    if idx < 0 or idx > len(my_list):
        return None

    for i, ch in enumerate(my_list):
        if i == idx:
            result = ch

    return result
