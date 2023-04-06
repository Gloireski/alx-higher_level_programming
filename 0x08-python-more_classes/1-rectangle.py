#!/usr/bin/python3


class Rectangle:
    """complete rectangle"""
    def __init__(self, width=0, height=0):
        """ constructeur """
        self.width = width
        self.height = height

    def width(self):
        """returns the porperty width"""
        return self.__width

    def width(self, value):
        """ setter of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """returns the porperty height"""
        return self.___height

    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
