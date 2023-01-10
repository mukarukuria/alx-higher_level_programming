#!/usr/bin/python3
def element_at(my_list, idx):
    result = 0
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    else:
        for i, ch in enumerate(my_list):
            if i == idx:
                result = ch

        return result
