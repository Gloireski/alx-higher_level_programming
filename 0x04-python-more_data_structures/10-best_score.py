#!/usr/bin/python3

def best_score(a_dictionary):
    a = ''
    bigg = 0
    if not a_dictionary:
        return None
    else:
        return max(a_dictionary, key=a_dictionary.get)
