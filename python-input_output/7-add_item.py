#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        coll_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        coll_data = []

    for arg in sys.argv[1:]:
        coll_data.append(arg)

    save_to_json_file(coll_data, "add_item.json")
