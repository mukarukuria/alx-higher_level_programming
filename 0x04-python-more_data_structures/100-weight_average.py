#!/usr/bin/python3
def weight_average(my_list=[]):
    ans = 1
    prod = 0
    if len(my_list) == 0:
        return 0

    
    for i, el in enumerate(my_list):
        score, weight = el
        ans = (score * weight) + ans
        prod += weight 
    return (ans/ prod)
