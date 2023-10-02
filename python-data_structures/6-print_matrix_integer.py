#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    max_width = 0
    for row in matrix:
        for num in row:
            max_width = max(max_width, len(str(num)))
    for row in matrix:
        for num in row:
            print("{:>{width}}".format(num, width=max_width), end=" ")
        print()
