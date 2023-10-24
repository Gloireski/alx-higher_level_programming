#!/usr/bin/python3

"""
    first class
"""


class Square:
    """define  class with size attr with validation"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self):
        try:
            if isinstance(value, tuple) and len(value) == 2 and\
                    value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers", end='')
            raise Exception

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print("" * self.__position[1])
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
