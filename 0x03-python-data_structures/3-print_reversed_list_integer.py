#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("", end='')
    else:
        my_list.reverse()
        for c in range(0, len(my_list)):
            print("{:d}".format(my_list[c]))
