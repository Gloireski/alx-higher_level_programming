#!/usr/bin/python3
# 2-matrix_divided.py
"""
    File name: 3-say_my_name.py
    Say my name: Function that prints 
    My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name="")
    You are not allowed to import any module
"""

def say_my_name(first_name, last_name=""):
    """
        prints My name is <first name> <last name>
        Raises:
            TypeError: first_name must be a string or
            last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
