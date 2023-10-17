#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


import json


def from_json_string(my_str):
    """
    'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    return json.loads(my_str)
