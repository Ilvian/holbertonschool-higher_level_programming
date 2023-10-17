#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


import json


def save_to_json_file(my_obj, filename):
    """
    'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
