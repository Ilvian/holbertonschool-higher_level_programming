# Python - Test-driven development ( Learning Objectives )

What’s an interactive test
Why tests are important
How to write Docstrings to create tests
How to write documentation for each module and function
What are the basic option flags to create tests
How to find edge cases

1. **What’s an interactive test?**

An interactive test is any testing process that requires human involvement, often in the form of inputs, decisions, or judgments. 

**Example**: Consider a CAPTCHA test on websites to differentiate between humans and bots. A user is shown distorted text or images and is asked to identify them. This requires human interpretation and cannot be effectively automated.

2. **Why tests are important?**

Tests ensure that software operates as intended, catches regressions, and provides a safety net for developers.

**Example**: Imagine an online banking system. Without testing, a minor bug could lead to significant financial losses or breaches of sensitive information. Regularly testing functions like balance transfers, password updates, or statement generations ensures that the bank's digital services operate safely and efficiently.

3. **How to write Docstrings to create tests?**

Python's `doctest` module allows you to embed test cases within docstrings. 

**Example**:
```python
def multiply(a, b):
    """
    Returns the product of two numbers.
    
    >>> multiply(2, 3)
    6
    >>> multiply(-1, 5)
    -5
    """
    return a * b
```

By running `doctest`, Python will execute the provided examples and verify that the outputs match the documented values.

4. **How to write documentation for each module and function?**

Well-documented code is essential for maintenance, collaboration, and usage.

**Module-level**:

```python
"""
This module provides arithmetic operations for basic calculations.

Example:
    >>> from arithmetic import add
    >>> add(2,3)
    5
"""
```

**Function-level**:

```python
def subtract(a, b):
    """
    Returns the result of subtracting b from a.
    
    Parameters:
    - a (int/float): The number from which another number is to be subtracted.
    - b (int/float): The number to be subtracted from the first number.
    
    Returns:
    int/float: Result of the subtraction.
    
    Example:
    >>> subtract(5, 3)
    2
    """
    return a - b
```

5. **What are the basic option flags to create tests?**

Using Python's `unittest` as an example:

- `-v` or `--verbose`: Outputs more detailed information about each test run.
  
**Example**: Without `-v`, `unittest` might only tell you how many tests passed/failed. With `-v`, you can see details of each test case.

- `discover`: Searches for test scripts in the directory.

**Example**: If you have multiple test files like `test_model.py`, `test_controller.py`, etc., the `discover` flag will find and run all these tests.

6. **How to find edge cases?**

Edge cases test the boundaries and outliers of a system.

**Examples**:

- **Boundary Values**: If a function is supposed to work for numbers between 1-100, test with values 0, 1, 100, and 101.

- **Data Types**: If an API expects a string input, try sending integers, lists, or null values. For example, if an endpoint expects a name like "John", try sending 12345 or even special characters.

- **Invalid Input**: If you have a form that expects an email, try inputting without the "@" symbol or even scripting tags to test for script injection vulnerabilities.

By thinking outside the usual scenarios and considering "what could go wrong", you can better identify and address potential edge cases.
