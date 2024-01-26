#!/usr/bin/python3
# this module defines a function


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    for i in range(len(list_of_integers) - 1):
        if (list_of_integers[i] >= list_of_integers[i-1]) and
        (list_of_integers[i] >= list_of_integers[i+1]):
            return list_of_integers[i]
