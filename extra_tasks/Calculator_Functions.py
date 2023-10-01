def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factorial(num):
    if num < 0:
        return "Invalid input (negative number)"
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def display_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Check if a number is prime")
    print("6. Calculate factorial")
    print("7. Exit")
