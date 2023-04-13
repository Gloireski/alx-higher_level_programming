#!/usr/bin/python3
# 10-square.py
"""
    File name : 10-square.py
    Requirement:none
"""
Rectangle =  __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class Square
    """
    def __init__(self, size):
        """
            construc
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            Represent area
            Return:
            width * height
        """
        return self.__size ** 2
