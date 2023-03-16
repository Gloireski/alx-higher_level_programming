#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for el in range(len(my_list)):
        if new_list[el] == search:
            new_list[el] = replace
    return new_list
