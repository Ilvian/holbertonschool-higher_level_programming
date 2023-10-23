#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if args:
            a_index = 0
            for arg in args:
                if a_index == 0:
                    self.id = arg
                elif a_index == 1:
                    self.size = arg
                elif a_index == 2:
                    self.x = arg
                elif a_index == 3:
                    self.y = arg
                a_index += 1

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
