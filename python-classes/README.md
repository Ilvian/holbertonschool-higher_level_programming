# Python - Classes and Objects ( Learning Objectives )

What is OOP
“first-class everything”
What is a class
What is an object and an instance
What is the difference between a class and an object or instance
What is an attribute
What are and how to use public, protected and private attributes
What is self
What is a method
What is the special __init__ method and how to use it
What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
What is the difference between an attribute and a property in Python
What is the Pythonic way to write getters and setters in Python
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to object and classes
What is the __dict__ of a class and/or instance of a class and what does it contain
How does Python find the attributes of an object or class
How to use the getattr function

1. **OOP**: Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes), and code in the form of procedures (methods).

2. **"first-class everything"**: This means that everything in a programming language is treated as a first-class citizen. In Python, functions, classes, and basic data types are all first-class citizens.

3. **Class**: A class is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that its objects will have.

4. **Object and Instance**: An object is a particular instantiation of a class. "Instance" and "object" are often used interchangeably.

5. **Difference between a Class and an Object or Instance**: A class is a blueprint, while an object or instance is a single, concrete realization of that blueprint.

6. **Attribute**: An attribute is a variable that belongs to an object (or class).

7. **Public, Protected, and Private Attributes**: 
   - **Public**: Can be accessed from outside the class. In Python, all member variables are public by default.
   - **Protected**: Should not be accessed outside the class but can be. In Python, prefixing a variable with an underscore (`_var`) suggests it's protected.
   - **Private**: Should not be accessed outside the class. In Python, prefixing a variable with two underscores (`__var`) makes it private.

8. **Self**: In Python, `self` is a reference to the instance of the object itself. It's used in method definitions.

9. **Method**: A function that belongs to a class or an object.

10. **The special `__init__` method**: This is the initializer method in Python, similar to a constructor in other languages. It gets called when you create a new instance of a class.

11. **Data Abstraction, Data Encapsulation, and Information Hiding**:
   - **Data Abstraction**: Showing essential features without including background details.
   - **Data Encapsulation**: Wrapping data (attributes) and the methods that operate on the data into a single unit (class).
   - **Information Hiding**: Making certain details invisible to the outside world, ensuring only specific data is exposed.

12. **Property**: In Python, a property is a special type of attribute that is accessed using method-like syntax but doesn't require method call syntax.

13. **Difference between an Attribute and a Property in Python**: An attribute is a variable stored in an instance or class, while a property is a way to access an attribute with getter, setter, and deleter methods.

14. **Pythonic way to write getters and setters**: Use the `property` decorator.
```python
class MyClass:
    def __init__(self, x):
        self._x = x
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
```

15. **Dynamically create arbitrary new attributes for existing instances of a class**: You can dynamically add attributes to an object by simply assigning to them.
```python
obj = MyClass(10)
obj.new_attribute = "Hello"
```

16. **Bind attributes to object and classes**: As shown in the previous example, attributes can be bound to an instance. For classes, you define them in the class definition or bind them later with `MyClass.new_class_attribute = value`.

17. **`__dict__` of a class and/or instance of a class**: It's a dictionary that contains the namespace of the class or instance. It holds all the attributes and their values.

18. **How does Python find the attributes of an object or class**: Python looks in the object's (or class's) `__dict__`, and if it doesn't find it, it goes up the inheritance chain.

19. **Using the `getattr` function**: `getattr` fetches an attribute from an object.
```python
getattr(obj, 'attribute_name', default_value)
```
If the attribute isn't found, it returns the `default_value`. If `default_value` isn't provided and the attribute isn't found, it raises an `AttributeError`.
