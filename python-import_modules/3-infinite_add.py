#!/usr/bin/python3
from sys import argv
sum = 0
if __name__ == "__main__":
    for num in argv[1:]:
        sum += int(num)
print(sum)
