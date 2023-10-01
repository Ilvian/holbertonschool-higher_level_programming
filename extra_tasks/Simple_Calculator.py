#!/usr/bin/env python3
import Calculator_Functions as CF
def main():
    while True:
        CF.display_menu()
        choice = input("Choose an operation: ")

        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {CF.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {CF.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {CF.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {CF.divide(num1, num2)}")
        elif choice == '5':
            num = int(input("Enter number: "))
            if CF.is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        elif choice == '6':
            num = int(input("Enter number: "))
            print(f"Result: {CF.factorial(num)}")
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please select a number from the menu.")
        print()
main()
