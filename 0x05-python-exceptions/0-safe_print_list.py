#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i, el in enumerate(my_list):
            if i == x:
                break
            else:
                print("{}".format(el), end="")
            count += 1
        print("")
        return count
    except(TypeError, ValueError):
        print("Error occured for some reason")
