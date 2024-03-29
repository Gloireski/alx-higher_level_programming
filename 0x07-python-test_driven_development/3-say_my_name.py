#!/usr/bin/python3
# 3-say_my_name.py
# Belem Gloire BEKOUTOU
"""Define say my name"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>.


        Args:
            first_name (str): The first name to print.
            last_name (str): The last name to print.
        Raises:
            TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
