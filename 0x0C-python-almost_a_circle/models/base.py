#!/usr/bin/python3
# base.py
"""
    Filename: base.py
    Define base class
"""


class Base(object):
    """
        Base: classe de Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            __init__: constructeur

            Args:
            id (int): Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
