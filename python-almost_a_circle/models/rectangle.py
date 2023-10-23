#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
from models.base import Base


class Rectangle(Base):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
