#!/usr/bin/python3

def best_score(a_dictionary):
    a = ''
    bigg = 0
    if a_dictionary is None:
        return 'None'
    for k, v in a_dictionary.items():
        if v > bigg:
            bigg = v
            a = k
    return a
