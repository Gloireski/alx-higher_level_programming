#!/usr/bin/python3

def no_c(my_string):
    list_str = ''
    for el in my_string:
        if el != 'c' and el != 'C':
            list_str = list_str + el
    list_str
    return list_str
