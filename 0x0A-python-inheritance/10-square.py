#!/usr/bin/python3
# 10-square.py
# Belem Gloire BEKOUTOU
"""square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle based class"""

    def __init__(self, size):
        """Intialize a new square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
