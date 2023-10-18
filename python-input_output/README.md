# Python - Input/Output ( Learning Objectives )

---

**How to open a file in Python:**

In Python, you can open a file using the built-in `open()` function. The basic syntax is:

```python
file = open('filename.txt', 'mode')
```

Where:

1. `'filename.txt'` is the name of the file you want to open. You can include a full path if the file is not in the same directory as your script.
2. `'mode'` specifies how you want to open the file. The most common modes are:
   - `'r'`: Read mode (default). Opens the file for reading.
   - `'w'`: Write mode. Opens the file for writing (creates a new file or truncates an existing file).
   - `'a'`: Append mode. Opens the file for writing (creates a new file or appends to an existing file).
   - `'b'`: Binary mode. Read or write the file in binary mode (e.g., `'rb'` or `'wb'`).

Examples:

1. Opening a file for reading:

```python
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
```

2. Opening a file for writing:

```python
with open('filename.txt', 'w') as file:
    file.write('Hello, World!')
```

3. Opening a file for appending:

```python
with open('filename.txt', 'a') as file:
    file.write('\nAppended text.')
```

Using the `with` statement (as shown in the examples) is recommended because it ensures that the file is properly closed after the block of code is executed.

---

**How to write text in a file:**

To write text to a file in Python, you use the `write()` method of a file object. Here's a step-by-step guide:

1. **Open the file in write or append mode**:
   - Use `'w'` mode to create a new file or overwrite an existing file.
   - Use `'a'` mode to append to an existing file (or create a new file if it doesn't exist).

2. **Write to the file**:
   - Use the `write()` method to write text to the file.

3. **Close the file**:
   - If you're using the `with` statement (recommended), the file will automatically close once the block is exited. Otherwise, use the `close()` method to close the file.

Here are some examples:

### Writing to a New File or Overwriting an Existing File
```python
# Using the 'with' statement (recommended)
with open('filename.txt', 'w') as file:
    file.write('This is the content of the file.')

# Without the 'with' statement
file = open('filename.txt', 'w')
file.write('This is the content of the file.')
file.close()
```

### Appending to an Existing File
```python
with open('filename.txt', 'a') as file:
    file.write('\nThis line will be appended to the file.')
```

---

**How to read the full content of a file:**

To read the full content of a file in Python, you use the `read()` method of a file object. Here's a step-by-step guide:

1. **Open the file in read mode**:
   - Use `'r'` mode (which is also the default mode).

2. **Read the content of the file**:
   - Use the `read()` method to read the entire content of the file into a string.

3. **Close the file**:
   - If you're using the `with` statement (recommended), the file will automatically close once the block is exited. Otherwise, use the `close()` method to close the file.

Here's an example:

### Reading the Entire Content of a File
```python
# Using the 'with' statement (recommended)
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)

# Without the 'with' statement
file = open('filename.txt', 'r')
content = file.read()
print(content)
file.close()
```

---

**How to read a file line by line:**

To read a file line by line in Python, you can iterate over the file object directly. When you loop over a file object, it yields each line in the file one by one.

Here's how you can do it:

### Using the `with` Statement (Recommended)

When you use the `with` statement, it ensures that the file is properly closed after the block of code is executed.

```python
with open('filename.txt', 'r') as file:
    for line in file:
        print(line, end='')  # `end=''` prevents double line breaks since `print` adds one by default
```

### Without the `with` Statement

If you don't use the `with` statement, remember to close the file manually using the `close()` method.

```python
file = open('filename.txt', 'r')
for line in file:
    print(line, end='')
file.close()
```

---

**How to move the cursor in a file:**

In Python, you can move the cursor (or the file pointer) within an open file using the `seek()` method of a file object. The position of the cursor determines from where the next read or write operation will start.

The `seek()` method takes two arguments:

1. `offset`: The number of bytes to move the cursor.
2. `whence` (optional): The reference point for the offset. It can have three values:
   - `0`: The beginning of the file (default).
   - `1`: The current file position.
   - `2`: The end of the file.

Here are some examples of using the `seek()` method:

### Move to the Beginning of the File

```python
with open('filename.txt', 'r') as file:
    file.seek(0)
    first_line = file.readline()
    print(first_line)
```

---

**What is JSON:**

JSON stands for **JavaScript Object Notation**. It's a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. JSON is a text format, independent of any language, but it uses conventions familiar to programmers of the C family of languages.

JSON data types include numbers, strings, booleans, arrays, objects, and null. For example:

```json
{
    "firstName": "John",
    "lastName": "Doe",
    "age": 25,
    "isStudent": false,
    "courses": ["Math", "English", "Programming"],
    "address": {
        "street": "21 Jump Street",
        "city": "New York",
        "postalCode": "10001"
    }
}
```

---

**What is serialization:**

Serialization is the process of converting a data structure or object state into a format that can be easily stored or transmitted and then reconstructed later. The main goal of serialization is to save the state of an object in order to recreate it when needed. The reverse process, converting a serialized format back into a data structure or object, is called deserialization.

---

**What is deserialization:**

Des

erialization is the reverse process of serialization. While serialization is about converting a data structure or object into a format suitable for storage or transmission, deserialization is about converting that format back into a usable data structure or object.

---

**How to convert a Python data structure to a JSON string:**

To convert a Python data structure to a JSON string, you can use the `json` module that comes with the Python standard library. Specifically, the `json.dumps()` function allows you to serialize a Python object into a JSON formatted string.

Example:

```python
import json

# Sample Python dictionary
data = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Physics"]
}

# Convert the dictionary to a JSON string
json_string = json.dumps(data)
```

---

**How to convert a JSON string to a Python data structure:**

To convert a JSON string into a Python data structure, you can use the `json` module provided in the Python standard library. Specifically, the `json.loads()` function is used to deserialize a JSON formatted string into a Python object.

Example:

```python
import json

# Sample JSON string
json_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Physics"]}'

# Convert the JSON string to a Python dictionary
data = json.loads(json_string)
```

---

