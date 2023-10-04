#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary)
    for i in key_list:
        if value == a_dictionary.get(i):
            del a_dictionary[i]
    return a_dictionary
