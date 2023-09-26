#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")
        for i in range(num_args):
            print(f"{i + 1}: {argv[i]}")


if __name__ == "__main__":
    main()
