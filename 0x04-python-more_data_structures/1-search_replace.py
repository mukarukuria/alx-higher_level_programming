#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i, el in enumerate(my_list):
        if el == search: 
            new_list.append(replace)
            continue
        new_list.append(el)

    return(new_list)
