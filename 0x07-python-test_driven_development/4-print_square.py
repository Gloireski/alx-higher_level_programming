#!/usr/bin/python3
# 4-print_square.py
"""
    File name: 4-print_square.py
    Print square: Function that prints a
    square with the character #.
    Prototype: def print_square(size)
    You are not allowed to import any module
"""


def print_square(size):
    """
        Prints a square with the character #.
        size is the size length of the square
        Raises:
            TypeError: size must be an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
