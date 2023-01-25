#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i, el in enumerate(my_list):
            count += 1
            if i == x:
                break
            else:  
                print("{}".format(el), end ="")
        print("")
        return count
    except:
        print("Error occured for some reason")
