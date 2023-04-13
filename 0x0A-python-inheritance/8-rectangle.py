#!/usr/bin/python3
# 8-rectangle.py
"""
    File name : 8-rectangle.py
    Requirement:none
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle
    """
    def __init__(self, width, height):
        """
            construc
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
