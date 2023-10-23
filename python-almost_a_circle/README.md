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
