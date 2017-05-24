#!/usr/bin/python3
"""
Defines class Rectangle with properties width and height
"""


class Rectangle:
    """ class variable, counts number of instances """
    number_of_instances = 0

    """ class variable, symbol used to print Rectangle """
    print_symbol = "#"

    """ Initializes Rectangle class """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """ returns area of the rectangle """
    def area(self):
        return self.__width * self.__height

    """ returns perimeter of the rectangle """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    """ prints rectangle with # """
    def __str__(self):
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return "\n"
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle.append(str(self.print_symbol))
                if i < self.__height - 1:
                    rectangle.append("\n")
        rectangle = "".join(rectangle)
        return rectangle

    """ returns string representation of rectangle able to
    recreated a new instance by using eval() """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """ destroys instance of Rectangle """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
