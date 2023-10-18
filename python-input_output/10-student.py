#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Student:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        emp_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    value = getattr(self, attr)
                    emp_dict[attr] = value
            return emp_dict
