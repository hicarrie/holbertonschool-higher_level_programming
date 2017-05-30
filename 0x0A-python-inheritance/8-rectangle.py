#!/usr/bin/python3
"""
Defines class BaseGeometry
"""


class BaseGeometry:
    """ public instance method area """
    def area(self):
        raise Exception("area() is not implemented")

    """ public instance method integer_validator """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""
Defines class Rectangle
"""


class Rectangle(BaseGeometry):
    """ initializes class """
    def __init__(self, width, height):
        if BaseGeometry.integer_validator(self, "width", width):
            self.width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.height = height
