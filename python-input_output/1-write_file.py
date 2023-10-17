#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def write_file(filename="", text=""):
    """
    'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
