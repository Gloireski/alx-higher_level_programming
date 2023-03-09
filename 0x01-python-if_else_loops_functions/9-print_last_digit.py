#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        ld = int(repr(number)[-1])
    return ld
