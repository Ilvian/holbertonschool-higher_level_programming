# PYTHON
Python is a computer programming language used to write software. It's known for being easy to read and write, making it a good choice for beginners and for various applications ranging from web development to scientific research.

---

## **1. Printing a simple string**:

**Code**:
```python
print("Hello, World!")
```

**Output**:
```
Hello, World!
```

**Explanation**:
The `print()` function directly outputs the text or string that's enclosed within the parentheses.

---

## **2. Printing a variable**:

**Code**:
```python
name = "Alice"
print(name)
```

**Output**:
```
Alice
```

**Explanation**:
Here, we first assign the string "Alice" to the variable `name`. We then print the value of the variable using the `print()` function.

---

## **3. Concatenating strings and variables**:

**Code**:
```python
name = "Bob"
print("Hello, " + name + "!")
```

**Output**:
```
Hello, Bob!
```

**Explanation**:
In this example, we concatenate or join strings using the `+` operator. We combine the string "Hello, " with the value of the variable `name`, and then append the "!" at the end.

---

## **4. Using formatted string literals (f-strings)**:

**Code**:
```python
name = "Charlie"
age = 30
print(f"Hello, {name}! You are {age} years old.")
```

**Output**:
```
Hello, Charlie! You are 30 years old.
```

**Explanation**:
F-strings, introduced in Python 3.6, allow for embedded expressions inside string literals. Expressions inside the curly braces `{}` are evaluated at runtime and then formatted using the given format string.

---

## **5. Using the `str.format()` method**:

**Code**:
```python
name = "David"
age = 25
print("Hello, {}! You are {} years old.".format(name, age))
```

**Output**:
```
Hello, David! You are 25 years old.
```

**Explanation**:
Using the `str.format()` method, you can substitute placeholders, denoted by `{}`, with the values you want to insert. The values are provided in the `format()` method in the order they should replace the placeholders.

---

## **6. Using the `%` operator (older formatting style)**:

**Code**:
```python
name = "Eve"
age = 20
print("Hello, %s! You are %d years old." % (name, age))
```

**Output**:
```
Hello, Eve! You are 20 years old.
```

**Explanation**:
The `%` operator is an older way of formatting strings in Python. `%s` is a placeholder for strings, and `%d` is a placeholder for integers. The values to be inserted are provided in a tuple after the `%` operator.

---

## **7. Printing multiple variables using commas**:

**Code**:
```python
x = 10
y = 20
print("The values are:", x, y)
```

**Output**:
```
The values are: 10 20
```

**Explanation**:
When you separate values with commas inside the `print()` function, Python prints each value separated by a space. This is a quick way to print multiple variables without the need for concatenation or formatting.

---

I hope these explanations provide a clear and structured way to introduce printing text and variables in Python to your students!
