#!/usr/bin/python3
# 0-rectangle.py
# Belem Gloire BEKOUTOU
"""Define a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle

            Args:
                width (int): The width of the new rectangle.
                height (int): The height of the new rectangle.
        """

        self.width = 0
        self.height = 0

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @property
    def height(self):
        """Returns height value"""
        return self.height

    @width.setter
    def width(self, value):
        """Sets value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value