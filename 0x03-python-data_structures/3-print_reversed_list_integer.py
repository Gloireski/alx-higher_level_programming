#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        print("", end='')
    my_list.reverse()
    for c in range(0, len(my_list)):
        print("{:d}".format(my_list[c]))
