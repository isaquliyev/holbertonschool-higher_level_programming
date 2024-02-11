#!/usr/bin/python3

"""
    The ``Square`` module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
            Set the side size of Square
        """
        self.__size = value

    def __str__(self):
        result = "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.size)
        return result
