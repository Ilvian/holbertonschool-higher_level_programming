#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
