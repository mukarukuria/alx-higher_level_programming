#!/usr/bin/python3
def weight_average(my_list=[]):
    ans = 1
    prod = 0
    if len(my_list) == 0:
        return 0
    total_weight = sum(weight for score, weight in my_list)
    weighted_sum = sum(score * weight for score, weight in my_list)
    return weighted_sum / total_weight
