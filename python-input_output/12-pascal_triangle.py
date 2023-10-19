#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def pascal_triangle(n):
    """
    'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) < n:
        prev_row = tri[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            next_val = prev_row[i] + prev_row[i + 1]
            new_row.append(next_val)
        new_row.append(1)
        tri.append(new_row)
    return tri
