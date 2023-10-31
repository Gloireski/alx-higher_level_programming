#!/usr/bin/python3
# 0-rectangle.py
# Belem Gloire BEKOUTOU
"""Define a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle

            Args:
                width (int): The width of the new rectangle.
                height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @property
    def height(self):
        """Returns height value"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets value to width"""
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """Sets value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a printable rep of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
        should return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangle instances"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() === rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
