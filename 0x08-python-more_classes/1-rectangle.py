#!/usr/bin/python3
# 1-rectangle.py
""" File name : 1-rectangle.py
    Real definition of a rectangle : class that defines a rectangle
    It is not allowed to import any module
"""


class Rectangle(object):
    """complete rectangle"""
    def __init__(self, width=0, height=0):
        """ constructeur """
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns the porperty width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set values to width
        Args:
            value (int): new value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the porperty height"""
        return self.___height

    @height.setter
    def height(self, value):
        """Set values to width
        Args:
            value (int): new value for width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
