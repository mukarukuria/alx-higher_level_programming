#!/usr/bin/python3
def best_score(a_dictionary):
    result = 0
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for i, el in enumerate(a_dictionary):
        if a_dictionary[el] > result:
            result = a_dictionary[el]
            winner = el
    return winner
