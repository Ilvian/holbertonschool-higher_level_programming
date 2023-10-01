# Python - Hello, World
# Objectives

* 1. How to use the Python interpreter?

The Python interpreter allows you to execute Python code interactively, line by line. Here's how you can use the Python interpreter:
- Open the Terminal or Command Prompt:
You'll need a command-line interface to run the Python interpreter. On most systems, you can find the Terminal (Unix/Linux) or Command Prompt (Windows) in your system's applications or programs.

- Start the Python Interpreter:
On Unix/Linux/macOS: Open the Terminal and type python or python3 (depending on your system's configuration) and press Enter.
On Windows: Open the Command Prompt and type python or python3 and press Enter. Make sure Python is installed and added to your system's PATH variable.
This will start the Python interpreter, and you'll see a Python prompt like >>>.

- Run Python Code:
You can now enter Python code directly into the interpreter. For example, you can type print("Hello, world!") and press Enter. The interpreter will execute the code and display the output, like this:
\\ >>> print("Hello, world!")
\\ Hello, world!

- Interactive Mode:
The Python interpreter is great for testing and experimenting with code. You can define variables, run functions, and see immediate results. For example:
\\ >>> x = 5
\\ >>> y = 10
\\ >>> x + y
\\ 15

- Multiline Statements: You can also write multi-line statements by using triple quotes (''' or """) or by adding a backslash (\) at the end of the line to indicate that the statement continues on the next line:
\\ >>> longString = "This is a long string that \
\\ ... continues on the next line."

- Exit the Interpreter: To exit the Python interpreter, you can type exit() or press Ctrl+D (Unix/Linux/macOS) or Ctrl+Z (Windows) followed by Enter. This will return you to the regular command prompt.
\\ >>> exit()

----------------------------------------------------------------------------------------------------------------------------------------------------

* 2. How to print text and variables using print?

The print() function in Python is used to output text and variables to the console.

- Printing a Simple String:
\\ print("Hello, World!")

- Printing Multiple Strings:
\\ print("Hello", "World!")

- Printing Variables:
\\ greeting = "Hello"
\\ name = "Alice"
\\ print(greeting, name)

- Concatenating Strings in Print:
\\ greeting = "Hello"
\\ name = "Alice"
\\ print(greeting + ", " + name + "!")

- Using f-strings (Python 3.6+):
\\ name = "Alice"
\\ age = 30
\\ print(f"My name is {name} and I am {age} years old.")

- Using str.format() method:
\\ name = "Alice"
\\ age = 30
\\ print("My name is {} and I am {} years old.".format(name, age))

- Using % formatting:
\\ name = "Alice"
\\ age = 30
\\ print("My name is %s and I am %d years old." % (name, age))

- To print a double-quote inside a string, use an escape character (\):
\\ print("She said, \"Hello, World!\"")

- To print a single-quote inside a string enclosed with single-quotes, use an escape character:
\\ print('She said, \'Hello, World!\'')

- To print a backslash, double it (\\):
\\ print("This is a backslash: \\")

- By default, print() ends with a newline character. If you want to change the end character, you can use the end parameter:
\\ print("Hello", end=" ")
\\ print("World!")

- The sep parameter determines the character(s) used between multiple items:
\\ print("Hello", "World", sep="-")

----------------------------------------------------------------------------------------------------------------------------------------------------

3. How to use strings?

Strings are sequences of characters. In Python, you can represent strings using either single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`). Here's a guide on how to use strings in Python:

1. **Creating Strings**:
   ```python
   string1 = 'Hello, World!'
   string2 = "Python is fun."
   string3 = '''Triple quotes can be used
                for multi-line strings.'''
   string4 = """This is also a
                multi-line string."""
   ```

2. **Accessing Characters in a String** (using indexing):
   ```python
   my_string = "Hello"
   first_char = my_string[0]   # 'H'
   last_char = my_string[-1]  # 'o'
   ```

3. **Slicing Strings**:
   ```python
   my_string = "Python"
   slice1 = my_string[1:4]  # 'yth' (start from index 1 up to, but not including, index 4)
   slice2 = my_string[:3]   # 'Pyt' (start from the beginning up to index 3)
   slice3 = my_string[3:]   # 'hon' (start from index 3 to the end)
   ```

4. **String Concatenation**:
   ```python
   str1 = "Hello"
   str2 = "World"
   combined = str1 + ", " + str2 + "!"  # "Hello, World!"
   ```

5. **String Repetition**:
   ```python
   repeated = "abc" * 3  # 'abcabcabc'
   ```

6. **String Length**:
   ```python
   length = len("Hello")  # 5
   ```

7. **String Methods**:
   - Convert to uppercase: 
     ```python
     "hello".upper()  # 'HELLO'
     ```
   - Convert to lowercase: 
     ```python
     "HELLO".lower()  # 'hello'
     ```
   - Capitalize:
     ```python
     "hello world".capitalize()  # 'Hello world'
     ```
   - Check if it starts/ends with a substring:
     ```python
     "Hello".startswith("He")  # True
     "Hello".endswith("lo")    # True
     ```
   - Find the index of a substring:
     ```python
     "Hello".find("l")  # 2 (returns the index of the first occurrence)
     ```
   - Replace a substring:
     ```python
     "Hello, World!".replace("World", "Python")  # 'Hello, Python!'
     ```
   - Split a string into a list:
     ```python
     "apple,banana,orange".split(",")  # ['apple', 'banana', 'orange']
     ```

8. **String Membership**:
   ```python
   "ell" in "Hello"  # True
   "Wor" not in "Hello"  # True
   ```

9. **Escape Characters**:
   - Newline: `\n`
   - Tab: `\t`
   - Double Quote: `\"`
   - Single Quote: `\'`
   - Backslash: `\\`
   
   ```python
   print("This is a line.\nThis is another line.")
   print("This is a tab:\t* after tab.")
   ```

10. **Raw Strings**:
   - Sometimes, you don’t want characters prefaced by `\` to be interpreted as special characters. You can use raw strings by adding an `r` before the first quote:
     ```python
     raw_string = r"This is a \n raw string."
     print(raw_string)  # This is a \n raw string.
     ```

11. **String Formatting**:
   - Using f-strings (Python 3.6+):
     ```python
     name = "Alice"
     age = 30
     print(f"{name} is {age} years old.")
     ```
   - Using `str.format()`:
     ```python
     "{0} is {1} years old.".format(name, age)
     ```

12. **String Immutability**:
   Strings in Python are immutable, which means you cannot modify an existing string in place. However, you can create a new string based on modifications to an old one.

This gives you a foundational understanding of strings in Python, but it's important to note that Python provides many more methods and functionalities related to strings. Always refer to the official Python documentation for comprehensive details.

----------------------------------------------------------------------------------------------------------------------------------------------------

# What are indexing and slicing in Python?

In Python, indexing and slicing are used to access, modify, or extract specific elements or subsequences from iterable data structures like strings, lists, and tuples. Let's delve deeper into both concepts:

### 1. Indexing:

Indexing refers to accessing a single element of an iterable based on its position. In Python, indexing is zero-based, meaning the first element is at index `0`, the second is at index `1`, and so on.

- **Positive Indexing**: Starts counting from the beginning of the iterable.
  ```python
  my_list = [10, 20, 30, 40, 50]
  first_element = my_list[0]  # 10
  third_element = my_list[2]  # 30
  ```

- **Negative Indexing**: Starts counting from the end of the iterable.
  ```python
  last_element = my_list[-1]  # 50
  second_to_last_element = my_list[-2]  # 40
  ```

### 2. Slicing:

Slicing allows you to access a subrange or a subsequence from an iterable. The syntax for slicing is:
```python
iterable[start:stop:step]
```
- `start`: The beginning index of the slice. If omitted, it defaults to `0` for positive steps and `-1` for negative steps.
- `stop`: The ending index of the slice, which is not included in the result. If omitted, it defaults to the end of the iterable for positive steps and the beginning for negative steps.
- `step`: Determines the increment between indices. If omitted, it defaults to `1`.

Here are some examples using slicing:

```python
my_list = [0, 1, 2, 3, 4, 5]

# Extract elements from index 1 up to (but not including) index 4
slice1 = my_list[1:4]  # [1, 2, 3]

# Extract the first three elements
slice2 = my_list[:3]   # [0, 1, 2]

# Extract elements starting from index 2 to the end
slice3 = my_list[2:]   # [2, 3, 4, 5]

# Extract every second element
slice4 = my_list[::2]  # [0, 2, 4]

# Reverse the list using slicing
reversed_list = my_list[::-1]  # [5, 4, 3, 2, 1, 0]
```

The same indexing and slicing concepts apply to strings:

```python
my_string = "PYTHON"

# Indexing
first_char = my_string[0]   # 'P'
last_char = my_string[-1]   # 'N'

# Slicing
slice_str1 = my_string[1:4]  # 'YTH'
slice_str2 = my_string[::2]  # 'PTO'
```

Remember:
- When using positive step values, the default start is `0`, and the default stop is the end of the iterable.
- When using negative step values, the default start is `-1`, and the default stop is the beginning of the iterable.

Using indexing and slicing effectively is fundamental when manipulating data structures in Python.

----------------------------------------------------------------------------------------------------------------------------------------------------

# What is the official Python coding style and how to check your code with pycodestyle?

In Python, indexing and slicing are used to access, modify, or extract specific elements or subsequences from iterable data structures like strings, lists, and tuples. Let's delve deeper into both concepts:

### 1. Indexing:

Indexing refers to accessing a single element of an iterable based on its position. In Python, indexing is zero-based, meaning the first element is at index `0`, the second is at index `1`, and so on.

- **Positive Indexing**: Starts counting from the beginning of the iterable.
  ```python
  my_list = [10, 20, 30, 40, 50]
  first_element = my_list[0]  # 10
  third_element = my_list[2]  # 30
  ```

- **Negative Indexing**: Starts counting from the end of the iterable.
  ```python
  last_element = my_list[-1]  # 50
  second_to_last_element = my_list[-2]  # 40
  ```

### 2. Slicing:

Slicing allows you to access a subrange or a subsequence from an iterable. The syntax for slicing is:
```python
iterable[start:stop:step]
```
- `start`: The beginning index of the slice. If omitted, it defaults to `0` for positive steps and `-1` for negative steps.
- `stop`: The ending index of the slice, which is not included in the result. If omitted, it defaults to the end of the iterable for positive steps and the beginning for negative steps.
- `step`: Determines the increment between indices. If omitted, it defaults to `1`.

Here are some examples using slicing:

```python
my_list = [0, 1, 2, 3, 4, 5]

# Extract elements from index 1 up to (but not including) index 4
slice1 = my_list[1:4]  # [1, 2, 3]

# Extract the first three elements
slice2 = my_list[:3]   # [0, 1, 2]

# Extract elements starting from index 2 to the end
slice3 = my_list[2:]   # [2, 3, 4, 5]

# Extract every second element
slice4 = my_list[::2]  # [0, 2, 4]

# Reverse the list using slicing
reversed_list = my_list[::-1]  # [5, 4, 3, 2, 1, 0]
```

The same indexing and slicing concepts apply to strings:

```python
my_string = "PYTHON"

# Indexing
first_char = my_string[0]   # 'P'
last_char = my_string[-1]   # 'N'

# Slicing
slice_str1 = my_string[1:4]  # 'YTH'
slice_str2 = my_string[::2]  # 'PTO'
```

Remember:
- When using positive step values, the default start is `0`, and the default stop is the end of the iterable.
- When using negative step values, the default start is `-1`, and the default stop is the beginning of the iterable.

Using indexing and slicing effectively is fundamental when manipulating data structures in Python.
