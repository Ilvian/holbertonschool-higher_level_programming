# Python - More Classes and Objects
## ( Learning Objectives )

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
What are the special __str__ and __repr__ methods and how to use them
What is the difference between __str__ and __repr__
What is a class attribute
What is the difference between a object attribute and a class attribute
What is a class method
What is a static method
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to object and classes
What is and what does contain __dict__ of a class and of an instance of a class
How does Python find the attributes of an object or class
How to use the getattr function

1. **What is OOP?**  
OOP stands for Object-Oriented Programming. It's a programming paradigm that's based on the concept of "objects" which can contain data, in the form of fields, and code, in the form of procedures. The goal of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

2. **“first-class everything”**  
In some programming languages, "first-class" refers to entities which can be passed as arguments, returned from a function, assigned to variables, etc. In Python, functions are first-class citizens, meaning you can pass them around as arguments, return them, etc. However, the term "first-class everything" isn't a standard term in Python or OOP. It may be referring to the idea that everything (functions, classes, etc.) has a first-class status.

3. **What is a class?**  
A class is a blueprint for creating objects. It's a user-defined prototype from which objects can be created and defines the attributes and methods common to all objects of a certain kind.

4. **What is an object and an instance?**  
An object is a unique instance of a data structure defined by a class. "Instance" and "object" are used interchangeably, but strictly speaking, an instance refers to a single, unique unit of a class.

5. **Difference between a class and an object or instance?**  
A class is a blueprint or prototype. An object (or instance) is an individual realization of that blueprint.

6. **What is an attribute?**  
An attribute is a named property of a class. It represents some kind of data or state associated with objects of that class.

7. **Public, protected, and private attributes?**  
- **Public**: Can be accessed from any part of the program. In Python, all attributes are public by default.
- **Protected**: Meant to be accessed only from within the class or its subclasses. In Python, this is signified by a leading underscore (e.g., `_protectedVar`).
- **Private**: Should be accessed only within the class. In Python, signified by two leading underscores (e.g., `__privateVar`).

8. **What is `self`?**  
`self` refers to the instance on which a method is called. It's the first argument passed to any class method in Python.

9. **What is a method?**  
A method is a function defined within a class and is designed to operate on instance data.

10. **The special `__init__` method?**  
The `__init__` method in Python is a special method called a constructor. It gets called when a new instance of the class is created and initializes the attributes of the class.

11. **Data Abstraction, Data Encapsulation, and Information Hiding?**  
- **Data Abstraction**: The concept of representing essential features without including the background details.
- **Data Encapsulation**: The bundling of data and methods that operate on that data within a single unit (or object).
- **Information Hiding**: Restricting the details of an object to be hidden from the user and exposing only the necessary functionalities.

12. **What is a property?**  
In Python, a property is a special kind of attribute that is accessed using the same syntax as attribute access but is implemented using methods.

13. **Difference between an attribute and a property in Python?**  
While both can be accessed using the same syntax, an attribute is a variable that holds data, whereas a property uses methods to get, set, or delete a value, allowing for custom behavior.

14. **Pythonic way to write getters and setters?**  
The Pythonic way is to use properties using the `@property` decorator and the associated `@<attribute>.setter` decorator.

15. **Special `__str__` and `__repr__` methods?**  
Both methods are used to define human-readable and unambiguous string representations of objects. `__str__` is for the informal string representation (pretty print), and `__repr__` is for the formal (code-like) representation.

16. **Difference between `__str__` and `__repr__`?**  
`__str__` is meant for displaying to end-users while `__repr__` is more for developers (e.g., for debugging).

17. **What is a class attribute?**  
It's an attribute that belongs to the class rather than any particular object instance and is shared among all instances of the class.

18. **Difference between an object attribute and a class attribute?**  
Object attributes are specific to each instance of the class, while class attributes are shared among all instances.

19. **What is a class method?**  
A method that's bound to the class and not the instance. It takes `cls` (the class) as its first parameter. Decorated with `@classmethod`.

20. **What is a static method?**  
A method that doesn't modify or access instance-specific data or class data. Decorated with `@staticmethod`.

21. **Dynamically create arbitrary new attributes for existing instances of a class?**  
This can be done using the `setattr` function or direct assignment, e.g., `instance.new_attribute = value`.

22. **Binding attributes to objects and classes?**  
Attributes can be bound to instances using dot notation (e.g., `instance.attribute = value`) and to classes similarly (e.g., `Class.attribute = value`).

23. **What does `__dict__` contain?**  
For an instance, `__dict__` is a dictionary containing the instance's attributes. For a class, it contains attributes and methods of the class.

24. **How does Python find the attributes of an object or class?**  
Python looks up attributes by checking the instance's `__dict__`, then the class's `__dict__`, and then the `__dict__` of the class's bases in the method resolution order.

25. **How to use the `getattr` function?**  
`getattr` is used to get the value of an attribute. Syntax: `getattr(object, "attribute_name", default_value)`. If the attribute exists, it returns the attribute's value, otherwise, it returns the provided default value or raises an AttributeError if no default is given.

7. **Public, protected, and private attributes?**
```python
class SampleClass:
    public_var = "I'm public!"
    _protected_var = "I'm protected!"
    __private_var = "I'm private!"

obj = SampleClass()
print(obj.public_var)  # Outputs: I'm public!
print(obj._protected_var)  # Outputs: I'm protected!
# print(obj.__private_var)  # This will raise an AttributeError
```

8. **What is `self`?**
```python
class Car:
    def __init__(self, color):
        self.color = color  # 'self' refers to the instance being created

car1 = Car("red")
print(car1.color)  # Outputs: red
```

10. **The special `__init__` method?**
```python
class Dog:
    def __init__(self, name):
        self.name = name

buddy = Dog("Buddy")
print(buddy.name)  # Outputs: Buddy
```

13. **Difference between an attribute and a property in Python?**
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius  # this is an attribute

    @property
    def diameter(self):  # this is a property
        return self.radius * 2

c = Circle(5)
print(c.radius)    # Outputs: 5
print(c.diameter)  # Outputs: 10
```

14. **Pythonic way to write getters and setters?**
```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

p = Person(25)
print(p.age)  # Outputs: 25

# p.age = -1  # This will raise ValueError
```

15. **Special `__str__` and `__repr__` methods?**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

b = Book("1984", "George Orwell")
print(str(b))  # Outputs: '1984' by George Orwell
print(repr(b)) # Outputs: Book('1984', 'George Orwell')
```

17. **What is a class attribute?**
```python
class Cat:
    species = "Mammal"  # this is a class attribute

whiskers = Cat()
print(whiskers.species)  # Outputs: Mammal
```

18. **Difference between an object attribute and a class attribute?**
```python
class Dog:
    breed = "Canine"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

rex = Dog("Rex")
print(Dog.breed)  # Outputs: Canine
print(rex.name)   # Outputs: Rex
```

21. **Dynamically create arbitrary new attributes for existing instances of a class?**
```python
class Empty:
    pass

e = Empty()
e.new_attribute = "I was added dynamically!"
print(e.new_attribute)  # Outputs: I was added dynamically!
```

24. **How does Python find the attributes of an object or class?**
```python
class Animal:
    species = "Unknown"

class Bird(Animal):
    species = "Avian"

sparrow = Bird()
print(sparrow.species)  # Outputs: Avian because Python first looks in the instance, then in its class, then in its parent class.
```

25. **How to use the `getattr` function?**
```python
class Robot:
    purpose = "Helping humans"

print(getattr(Robot, "purpose", "Unknown purpose"))  # Outputs: Helping humans
print(getattr(Robot, "origin", "Unknown origin"))    # Outputs: Unknown origin
```
