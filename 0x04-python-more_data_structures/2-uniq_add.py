#!/usr/bin/python3

def uniq_add(my_list=[]):
    s = set(my_list)
    result = 0
    for un in s:
        result = result + un
    return result
