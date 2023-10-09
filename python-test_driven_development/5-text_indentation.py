#!/usr/bin/python3
def text_indentation(text):
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
