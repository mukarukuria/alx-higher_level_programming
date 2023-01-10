#!/usr/bin/python3
def max_integer(my_list=[]):
    big = my_list[0]

    if len(my_list) == 0:
        return None
    else:
        for i, el in enumerate(my_list):
            if el > big:
                big = el

        return big
