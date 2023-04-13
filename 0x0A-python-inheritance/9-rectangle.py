#!/usr/bin/python3
# 8-rectangle.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    File name : 8-rectangle.py
    Requirement:none
"""


class Rectangle(BaseGeometry):
    """
        class Rectangle
    """
    def __init__(self, width, height):
        """
            construc
        """
        self.width = width
        self.height = height

    def area(self):
        """Represent area
        Raises:
            Exception: [area() is not implemented]
        """
        return self.__width * self.__height

    def __str__(self):
        """
        """
        return "[Rectangle] <{}>/<{}>".format(self.__width, self.__height)
