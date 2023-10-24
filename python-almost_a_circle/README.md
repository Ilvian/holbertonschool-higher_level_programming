# Python - Almost a circle

## Basic Concepts (Dont Forget)

## Learning Objectives

### **Serializing and Deserializing Custom Classes with JSON in Python**

When handling data in Python, there may arise a need to save the state of custom classes in a readable format, like JSON, and recover it later. JSON is an open-standard format that uses human-readable text to transmit data objects. In Python, while basic data types like numbers, strings, lists, and dictionaries can be directly serialized to JSON, custom classes need specialized handling. Here's how you can achieve this with a custom `Person` class:

#### **1. Defining the `Person` Class with Serialization and Deserialization Methods:**

The core idea here is to provide a method to convert the custom object to a basic Python data structure, like a dictionary, which can then be serialized to JSON. Conversely, another method will aid in converting a dictionary back to the object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        """Convert the object to a dictionary suitable for JSON serialization."""
        return {
            'name': self.name,
            'age': self.age
        }

    @classmethod
    def from_dict(cls, data):
        """Construct the object from a dictionary."""
        return cls(name=data['name'], age=data['age'])
```

`to_dict()` serves as the serializer, while `from_dict()` acts as the deserializer.

#### **2. Serializing and Saving to a File:**

The `json` module offers two main methods for this: `dumps()` for converting Python objects to JSON strings and `dump()` for writing these strings directly to files.

```python
import json

# Create an instance of the class
person = Person("Alice", 30)

# Serialize the object to a JSON string
serialized_person = json.dumps(person.to_dict())

# Save the serialized data to a file
with open("person.json", "w") as f:
    json.dump(person.to_dict(), f)
```

#### **3. Deserializing from a JSON String and Loading from a File:**

The counterparts to the serialization methods in the `json` module are `loads()` for reading JSON strings into Python objects and `load()` for reading JSON from files.

```python
# Deserialize the object from the JSON string
deserialized_data = json.loads(serialized_person)
deserialized_person = Person.from_dict(deserialized_data)

# Load the serialized data from a file and deserialize it
with open("person.json", "r") as f:
    loaded_data = json.load(f)
    loaded_person = Person.from_dict(loaded_data)
```

This approach allows you to serialize and deserialize custom classes in Python using JSON. If you find yourself dealing with more intricate cases, or you want a streamlined experience, consider libraries like `marshmallow` that offer enhanced serialization capabilities.


## **Understanding and Using `*args` in Python**

In Python, `*args` is a way to pass a variable number of arguments to a function. It allows you to pass any number of positional arguments to the function, which are then collected into a tuple.

### Usage of `*args`:

1. **In Function Definitions**:
   
   When defining a function, you can use `*args` to collect any additional positional arguments passed to the function.
   
   ```python
   def function_with_args(first_arg, *args):
       print("First argument:", first_arg)
       for arg in args:
           print("Another argument through *args:", arg)
   ```

   You can call this function with various numbers of arguments:
   
   ```python
   function_with_args("hello", "world", 42, True)
   ```

   Output:
   ```
   First argument: hello
   Another argument through *args: world
   Another argument through *args: 42
   Another argument through *args: True
   ```

2. **When Calling Functions**:
   
   You can use the `*` operator to unpack the elements of a list or tuple and pass them as separate positional arguments to a function.
   
   ```python
   def function(a, b, c):
       print(a, b, c)

   args = (1, 2, 3)
   function(*args)
   ```

   Output:
   ```
   1 2 3
   ```

### Important points:

1. Inside the function, `args` is a tuple containing all the passed positional arguments.
2. `*args` only collects **positional** arguments. To collect keyword (or named) arguments, you would use `**kwargs`.
3. The name `args` is just a convention. You could technically use any name, like `*varargs`, but `*args` is most commonly used.

Here's an example showing a combination of positional, `*args`, and `**kwargs`:

```python
def function(x, *args, **kwargs):
    print("x:", x)
    print("args:", args)
    print("kwargs:", kwargs)

function(1, 2, 3, 4, 5, a=6, b=7)
```

Output:
```
x: 1
args: (2, 3, 4, 5)
kwargs: {'a': 6, 'b': 7}
```

Remember, the real power of `*args` comes from its ability to make functions more flexible, allowing them to accept a varying number of arguments.


## **Understanding and Using `**kwargs` in Python**

In Python, `**kwargs` is a mechanism that allows a function to accept an arbitrary number of keyword arguments. The name `kwargs` stands for "keyword arguments." These keyword arguments are collected into a dictionary where the argument names are the keys, and their corresponding values are the dictionary values.

### Usage of `**kwargs`:

1. **In Function Definitions**:

   When defining a function, you can use `**kwargs` to capture any additional keyword arguments that are passed to the function.
   
   ```python
   def function_with_kwargs(**kwargs):
       for key, value in kwargs.items():
           print(f"Key: {key}, Value: {value}")
   ```

   You can call this function with various keyword arguments:

   ```python
   function_with_kwargs(first_name="John", last_name="Doe", age=30)
   ```

   Output:
   ```
   Key: first_name, Value: John
   Key: last_name, Value: Doe
   Key: age, Value: 30
   ```

2. **When Calling Functions**:

   You can use the `**` operator to unpack the contents of a dictionary and pass them as separate keyword arguments to a function.

   ```python
   def function(a, b, c):
       print(a, b, c)

   kwargs = {'a': 1, 'b': 2, 'c': 3}
   function(**kwargs)
   ```

   Output:
   ```
   1 2 3
   ```

### Important points:

1. Inside the function, `kwargs` is a dictionary containing all the passed keyword arguments.
2. `**kwargs` captures only **keyword** arguments that haven't been caught by other parameter names in the function definition.
3. The name `kwargs` is convention, but you could technically use any name, like `**keyargs`, though `**kwargs` is the most recognized.

Here's an example showing a combination of positional, `*args`, and `**kwargs`:

```python
def function(x, *args, **kwargs):
    print("x:", x)
    print("args:", args)
    print("kwargs:", kwargs)

function(1, 2, 3, 4, 5, a=6, b=7)
```

Output:
```
x: 1
args: (2, 3, 4, 5)
kwargs: {'a': 6, 'b': 7}
```

This mechanism makes functions in Python very flexible, allowing developers to create more generic functions or APIs that can accept a wide range of input parameters.
