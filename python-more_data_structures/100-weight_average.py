#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    dev = 0
    for i in my_list:
        total += i[0] * i[1]
        dev += i[1]
    return (total / dev)
