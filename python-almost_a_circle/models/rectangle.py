#!/usr/bin/python3

"""
    The ``2. First Rectangle`` module
"""


from models.base import Base


class Rectangle(Base):
    """
        Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
            Set the value for width
        """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
            Set the value for height
        """
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """
            Set the value for x
        """
        self.validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """
            Set the value for y
        """
        self.validator("y", value, True)
        self.__y = value

    def validator(self, attribute_name, value, can_be_zero=False):
        """
            Checks the value valid or not
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute_name))
        if not can_be_zero and value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))
        if can_be_zero and value < 0:
            raise ValueError("{} must be >= 0".format(attribute_name))
