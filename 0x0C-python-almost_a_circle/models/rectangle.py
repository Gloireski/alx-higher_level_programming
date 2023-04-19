#!/usr/bin/python3
# rectangle.py
"""
    Filename: rectangle.py
    Inherits from base class
"""
from models.base import Base


class Rectangle(Base):
    """
        Class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            __init__ constructeur

            Args:
                width, height, x, y, id
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ returns property width """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter

            Args:
                value to assign to width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ returns the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
            Args:
                value: new value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
            sets new value to x
            Args:
                value: new value to x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ returns value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
            sets new value to y
            Args:
                value: new value to y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value """
        return self.__width * self.__height

    def display(self):
        c = 0
        d = 1
        while (d <= self.__y):
            print("")
            d += 1
        while (c < self.__height):
            print(" " * self.x, end='')
            print("#" * self.__width)
            c += 1

    def __str__(self):
        """
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
