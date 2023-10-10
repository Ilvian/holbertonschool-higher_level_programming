#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def text_indentation(text):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    while i < length:
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print("\n\n", end='')
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
