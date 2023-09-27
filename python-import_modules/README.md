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

-----------------------------------------------------------------------------------------------------------------------
# myModule.py

def someFunction():
# Your code here

if __name__ == "__main__":
# This code will only run when the script is executed directly
# It won't run when this script is imported as a module

print("This code is executed only when the script is run directly.")

-----------------------------------------------------------------------------------------------------------------------

In this example, the code under the if __name__ == "__main__": block will only be executed if you run myModule.py directly. If you import myModule into another script, the code inside the if __name__ == "__main__": block will not run.
Example of how you can use the myModule:

-----------------------------------------------------------------------------------------------------------------------
# anotherScript.py
import myModule

myModule.someFunction()
# This will execute the function in myModule
# The code inside the if __name__ == "__main__": block in myModule will not run when imported.

-----------------------------------------------------------------------------------------------------------------------

7. How to use command line arguments with your Python programs?

Using command-line arguments in Python allows you to pass parameters or options to your Python scripts when you run them from the command line. Python provides the sys.argv list and the argparse module to handle command-line arguments.

- Method 1: Using sys.argv
The sys.argv list contains the command-line arguments passed to your Python script. The first element (sys.argv[0]) is the script name itself, and the rest of the elements are the arguments passed.

Import the sys module.
Access command-line arguments using sys.argv.

-----------------------------------------------------------------------------------------------------------------------
import sys

# Print the script name
print("Script name:", sys.argv[0])

# Print other command-line arguments
for arg in sys.argv[1:]:
    print("Argument:", arg)

# Output
Script name: myscript.py
Argument: arg1
Argument: arg2

-----------------------------------------------------------------------------------------------------------------------

- Method 2: Using argparse
The argparse module provides a more structured way to parse and handle command-line arguments. It allows you to define argument types, descriptions, and more.

Import the argparse module.
Create an ArgumentParser object and define your command-line arguments.
Parse the command-line arguments using parser.parseArgs().

-----------------------------------------------------------------------------------------------------------------------
import argparse

parser = argparse.ArgumentParser(description="Description of your script")

# Add positional arguments
parser.addArgument("arg1", type=int, help="Description of arg1")
parser.addArgument("arg2", type=str, help="Description of arg2")

# Add optional arguments
parser.addArgument("--optionalArg", type=float, default=0.0, help="Description of optional_arg")

args = parser.parseArgs()

# Access the parsed arguments
arg1 = args.arg1
arg2 = args.arg2
optionalArg = args.optionalArg

print("arg1:", arg1)
print("arg2:", arg2)
print("optionalArg:", optionalArg)

# If you run your script as python myscript.py 42 hello --optionalArg 3.14, the output will be:
arg1: 42
arg2: hello
optionalArg: 3.14

-----------------------------------------------------------------------------------------------------------------------

