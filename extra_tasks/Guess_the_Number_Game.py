#!/usr/bin/python3
import random
def guess_the_number():
    number = random.randint(1, 1000)
    print("# I have picked a number from 1 to 1000.")
    print("# You think you can find it?")
    while True:
        guess = int(input("Enter the number here: "))
        if guess > number:
            print("The number is lower.")
        elif guess < number:
            print("The number is higher.")
        else:
            print("CONGRATULATIONS you found it!!!!!!!!!!!!!")
            break
guess_the_number()
