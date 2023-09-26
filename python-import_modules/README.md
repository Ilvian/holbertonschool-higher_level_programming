Python - import & modules

Learning Objectives

1. Why Python programming is awesome?

Python is awesome because it's easy to learn, versatile, has a large and active community, a rich ecosystem of libraries, cross-platform compatibility, and is widely used in data science and machine learning, among other domains. It also offers excellent documentation, strong integration capabilities.

2. How to import functions from another file?

- Create the Python file with the functions you want to import: myFunctions.py
In this file, define the functions you want to use in other Python scripts.

-----------------------------------------------------------------------------------------------------------------------
# myFunctions.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

-----------------------------------------------------------------------------------------------------------------------

- Create the Python script where you want to use these functions: main.py

-----------------------------------------------------------------------------------------------------------------------
# main.py

import myFunctions
result1 = myFunctions.add(5, 3)
result2 = myFunctions.subtract(10, 4)
print(f"Addition result: {result1}")
print(f"Subtraction result: {result2}")

-----------------------------------------------------------------------------------------------------------------------

3. How to use imported functions?

In Python, you can import functions from modules or packages using the import keyword. There are different ways to import functions depending on what you need.

- Importing the entire module/package: \\ import moduleName \\
- Importing specific functions from a module: \\ from moduleName import functionName \\
- Importing a module with an alias (useful for modules with long names): \\ import moduleName as alias \\

Call the Imported Function: After importing the module or function, you can call it just like any other function in your Python script. You use the function name followed by parentheses, and you can pass any required arguments inside the parentheses.

- Here's an example of importing and using the math module/package to calculate the square root of a number in Python:

-----------------------------------------------------------------------------------------------------------------------
# Importing the math module/package
import math

# Using a function from the math module/package
# Calls the sqrt function to calculate the square root of 25
result = math.sqrt(25)

# Prints the result (5.0)
print(result)

-----------------------------------------------------------------------------------------------------------------------

- Here's an example of importing a specific function from the random module/package:

-----------------------------------------------------------------------------------------------------------------------
# Importing the randint function from the random module
from random import randint

# Using the imported function to generate a random number between 1 and 10
randomNumber = randint(1, 10)

# Prints a random number between 1 and 10
print(randomNumber)

-----------------------------------------------------------------------------------------------------------------------

4. How to create a module?

- Create a Python File: Start by creating a new Python file with a .py extension. This file will become your module.
- Define Functions and Variables: Inside the Python file, define the functions, classes, or variables that you want to include in your module.

-----------------------------------------------------------------------------------------------------------------------
# myModule.py

def sayHello(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

myVariable = 42

-----------------------------------------------------------------------------------------------------------------------

- Using the Module: To use your module in another Python script, you need to import it.

-----------------------------------------------------------------------------------------------------------------------
# main.py

import myModule

result = myModule.sayHello("Alice")
print(result)
# Output: Hello, Alice!

sumResult = myModule.add(10, 20)
print(sumResult)
# Output: 30

print(myModule.myVariable)
# Output: 42

-----------------------------------------------------------------------------------------------------------------------

5. How to use the built-in function dir()?

The dir() function in Python is a built-in function that returns a list of all valid attributes, methods, and properties of an object. It can be useful for introspection and exploring the available functionality of objects, including modules, classes, and instances.

- Syntax: \\ dir([object]) \\
- object (optional): This parameter specifies the object for which you want to retrieve the attributes and methods. If object is not provided, dir() returns a list of names in the current local scope.

- Example 1: Using dir() without an object

-----------------------------------------------------------------------------------------------------------------------
# Without an object, dir() returns names in the current local scope
namesInCurrentScope = dir()
print(namesInCurrentScope)

-----------------------------------------------------------------------------------------------------------------------

- Example 2: Using dir() with an object

-----------------------------------------------------------------------------------------------------------------------
# Create a simple class
class MyClass:
    def __init__(self):
        self.my_attribute = 42
    
    def my_method(self):
        return "Hello, World!"

# Create an instance of the class
obj = MyClass()

# Use dir() to list attributes and methods of the object
objectAttributesAndMethods = dir(obj)
print(objectAttributesAndMethods)

-----------------------------------------------------------------------------------------------------------------------

6. How to prevent code in your script from being executed when imported?

To prevent code in your script from being executed when imported as a module, you can use a special Python variable called __name__. When a Python script is executed, the __name__ variable is set to "__main__". However, when a script is imported as a module in another script, the __name__ variable is set to the name of the script/module.
