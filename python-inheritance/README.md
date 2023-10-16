# Python - Inheritance ( Learning Objectives )

1. **What is a superclass, baseclass or parentclass**:

In object-oriented programming (OOP) terminology, a superclass, base class, or parent class refers to a class that is extended or inherited by one or more subclasses (child classes). When a class inherits from another class, it adopts the attributes and methods of the parent class, potentially extending or overriding them.

In Python, you can create a superclass and then have other classes inherit from it. Here's a basic example to illustrate the concept:

```python
# Define the superclass (base class / parent class)
class Animal:
    def __init__(self, species):
        self.species = species
    
    def speak(self):
        pass

# Define a subclass (child class) that inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Define another subclass
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Testing
dog = Dog("Canine")
cat = Cat("Feline")

print(dog.speak())  # Outputs: Woof!
print(cat.speak())  # Outputs: Meow!
```

In this example:

- `Animal` is the superclass (or base class or parent class).
- `Dog` and `Cat` are subclasses (or child classes) of `Animal`.
- The `Dog` and `Cat` classes have inherited the `__init__` method from the `Animal` class.
- Both `Dog` and `Cat` classes have overridden the `speak` method of the `Animal` class.

This inheritance mechanism allows for creating a hierarchy of classes that share common attributes and behaviors, promoting code reuse and modularity.

2. **What is a subclass**:

In object-oriented programming (OOP), a subclass, also known as a derived class or child class, is a class that inherits from one or more classes (known as superclasses, base classes, or parent classes). This inheritance mechanism allows the subclass to adopt (or inherit) attributes and methods from the superclass, while also having the capability to introduce new attributes and methods or override the inherited ones.

The main benefits of using subclasses are:

1. **Code Reuse**: By inheriting attributes and methods from a parent class, you can reuse existing code without having to write it again.
   
2. **Modularity**: By organizing code into a class hierarchy, you can make the code more modular and easier to maintain and extend.
   
3. **Polymorphism**: This allows objects of different classes to be treated as objects of a common super class. For instance, if multiple subclasses override a method from the superclass, the most specific version of the method will be invoked depending on the actual object type at runtime.

Here's an example in Python:

```python
# Superclass (Base class or Parent class)
class Animal:
    def speak(self):
        pass

# Subclass (Child class)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Another Subclass
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create instances of the subclasses
dog = Dog()
cat = Cat()

print(dog.speak())  # Outputs: Woof!
print(cat.speak())  # Outputs: Meow!
```

In this example:
- `Dog` and `Cat` are subclasses of the `Animal` superclass.
- Both `Dog` and `Cat` override the `speak` method inherited from `Animal`.

By using subclasses, you can define a general behavior in the superclass (in this case, the `speak` method) and provide specific implementations in the subclasses (`Dog` and `Cat`).

3. **How to list all attributes and methods of a class or instance**:

You can use Python's built-in functions and modules to list all attributes and methods of a class or an instance. Here's how:

**For an instance using `dir()`**:
    The `dir()` function returns a list of names (as strings) of attributes and methods of the given object (and its classes).

    ```python
    class MyClass:
        def my_method(self):
            pass

    obj = MyClass()
    print(dir(obj))
    ```

    However, `dir()` will also list many built-in attributes and methods that are present due to the object's inheritance from the base Python object class. If you're interested in only the attributes and methods specific to your class, you might need to filter them out.

**For a class or instance using `vars()`**:
    The `vars()` function returns the `__dict__` attribute of its argument, which is a dictionary of the object's attributes (excluding methods).

    ```python
    class MyClass:
        class_attribute = 'class value'
        
        def __init__(self):
            self.instance_attribute = 'instance value'
            
        def my_method(self):
            pass

    obj = MyClass()
    print(vars(MyClass))  # Shows class attributes
    print(vars(obj))      # Shows instance attributes
    ```

**Using the `inspect` module**:
    The `inspect` module provides a more detailed approach to introspection. It can be especially useful if you want to differentiate between different kinds of attributes, like methods, regular attributes, etc.

    ```python
    import inspect

    class MyClass:
        class_attribute = 'class value'
        
        def __init__(self):
            self.instance_attribute = 'instance value'
            
        def my_method(self):
            pass

    # Get all members of the class
    all_members = inspect.getmembers(MyClass)

    # Filter only methods
    methods = [member for member in all_members if inspect.isfunction(member[1])]
    print("Methods:", methods)

    # Filter only attributes (excluding callable methods)
    attributes = [member for member in all_members if not callable(member[1])]
    print("Attributes:", attributes)
    ```

Remember, methods are also attributes in Python, but they are callable attributes. So when people differentiate between methods and attributes, they're often referring to the distinction between callable and non-callable attributes.

4. **When can an instance have new attributes**:

In Python, the flexibility of the object model allows instances of a class to gain new attributes dynamically, even after their initialization. Here's a detailed explanation:

4. **When can an instance have new attributes**:

    - **At Initialization**: When an instance is being created, you can assign attributes to it inside the `__init__` method.
      
      ```python
      class MyClass:
          def __init__(self):
              self.attribute1 = "value1"
      ```

    - **After Initialization**: Unlike some other object-oriented languages, Python allows you to add new attributes to an instance after it has been created. 
      
      ```python
      obj = MyClass()
      obj.attribute2 = "value2"  # Dynamically adding a new attribute to the instance
      ```

    - **Dynamically with `setattr`**: You can also use the `setattr` function to dynamically assign attributes to an instance.
      
      ```python
      setattr(obj, 'attribute3', 'value3')  # Dynamically adding attribute3 to obj
      ```

    - **Using Special Methods**: Classes can control attribute assignment using special methods like `__setattr__`. If you override these methods, be cautious, as they can alter the default behavior of attribute assignments.
      
      ```python
      class MyClass:
          def __setattr__(self, name, value):
              # Adding some custom behavior for attribute assignment
              print(f"Setting {name} to {value}")
              super().__setattr__(name, value)
              
      obj = MyClass()
      obj.attribute4 = "value4"  # This will trigger the custom __setattr__ method
      ```

    However, there are some caveats and considerations:

    - **Not Recommended for All Use Cases**: While you have the ability to dynamically add attributes, it's not always a good practice. It can make the code less predictable and harder to maintain. Typically, attributes that an instance should have are defined within the class to provide a clear and consistent structure.

    - **Watch Out for `__slots__`**: If a class defines a `__slots__` attribute, it explicitly declares which instance attributes are allowed. This prevents the dynamic creation of new attributes outside of those defined in `__slots__`.

      ```python
      class MyClass:
          __slots__ = ['attribute1']
          
      obj = MyClass()
      obj.attribute1 = "value1"
      # obj.attribute2 = "value2"  # This will raise an AttributeError
      ```

In conclusion, while Python provides the flexibility to add new attributes to instances dynamically, developers should use this feature judiciously and ensure that the overall design and intent of the class are maintained.

5. **How to inherit a class from another**:

Inheritance is a fundamental concept in object-oriented programming (OOP). In Python, inheritance is achieved by defining a new class that is built upon an existing class. This new class is known as the subclass or derived class, and the existing class is referred to as the superclass, base class, or parent class.

To make one class inherit from another in Python, you specify the superclass name in parentheses after the subclass name. Here's a step-by-step guide:

**Basic Inheritance**:
   A subclass inherits attributes and methods from the superclass.
   
   ```python
   class SuperClass:
       def method_in_super(self):
           return "Method in SuperClass"

   class SubClass(SuperClass):
       pass

   obj = SubClass()
   print(obj.method_in_super())  # Outputs: Method in SuperClass
   ```

   In the example above, `SubClass` inherits from `SuperClass`.

**Overriding Methods**:
   If you want to change the behavior of a method in the subclass that is inherited from the superclass, you can override it.
   
   ```python
   class SubClass(SuperClass):
       def method_in_super(self):
           return "Overridden method in SubClass"

   obj = SubClass()
   print(obj.method_in_super())  # Outputs: Overridden method in SubClass
   ```

**Extending Methods**:
   You can extend the behavior of inherited methods by invoking the method from the superclass using the `super()` function.
   
   ```python
   class SubClass(SuperClass):
       def method_in_super(self):
           original_output = super().method_in_super()
           return original_output + " but extended in SubClass"

   obj = SubClass()
   print(obj.method_in_super())  # Outputs: Method in SuperClass but extended in SubClass
   ```

**Multiple Inheritance**:
   Python supports multiple inheritance, where a subclass can inherit from multiple superclasses. You list the superclasses in parentheses separated by commas.
   
   ```python
   class ClassA:
       def method_a(self):
           return "Method in ClassA"

   class ClassB:
       def method_b(self):
           return "Method in ClassB"

   class SubClass(ClassA, ClassB):
       pass

   obj = SubClass()
   print(obj.method_a())  # Outputs: Method in ClassA
   print(obj.method_b())  # Outputs: Method in ClassB
   ```

**Use the `issubclass()` and `isinstance()` Functions**:
   - `issubclass(Class1, Class2)` checks if `Class1` is a subclass of `Class2`.
   - `isinstance(obj, Class)` checks if `obj` is an instance of `Class` or an instance of a subclass of `Class`.

In conclusion, inheritance allows for creating a class hierarchy where common behaviors can be defined in superclasses, and specialized behaviors can be defined in subclasses. This promotes code reuse and a modular structure.

6. **How to define a class with multiple base classes**:

In Python, a class can inherit from multiple base classes, a feature known as multiple inheritance. When defining a class with multiple base classes, you list the base classes in parentheses separated by commas.

Here's a basic example of multiple inheritance:

```python
class Base1:
    def method_from_base1(self):
        return "Method from Base1"

class Base2:
    def method_from_base2(self):
        return "Method from Base2"

class Derived(Base1, Base2):
    def method_from_derived(self):
        return "Method from Derived"

# Create an instance of the derived class
obj = Derived()

# Access methods from base classes and derived class
print(obj.method_from_base1())  # Outputs: Method from Base1
print(obj.method_from_base2())  # Outputs: Method from Base2
print(obj.method_from_derived())  # Outputs: Method from Derived
```

In this example, the `Derived` class inherits from both `Base1` and `Base2`.

**Points to Note:**

**Method Resolution Order (MRO)**: When multiple base classes have methods with the same name, the method of the first base class listed in the class definition will be used. The order in which base classes are listed in the class definition determines the method resolution order. You can inspect the MRO with the `mro()` method or the `__mro__` attribute:

    ```python
    print(Derived.mro())
    # Outputs: [<class '__main__.Derived'>, <class '__main__.Base1'>, <class '__main__.Base2'>, <class 'object'>]
    ```

**Use with Caution**: While multiple inheritance is a powerful feature, it can lead to complex and hard-to-maintain code if not used judiciously. It's often considered better practice to use composition (where classes are composed of several smaller classes or components) over multiple inheritance to achieve more flexible and maintainable designs.

**Mixins**: A common use case for multiple inheritance in Python is the use of mixins. A mixin is a base class that provides a specific piece of functionality but is not meant to stand alone. It's intended to be combined with other classes to add that functionality where needed.

Remember, when using multiple inheritance, it's crucial to understand the relationships and responsibilities of each base class to avoid potential pitfalls or unexpected behaviors.

7. **What is the default class every class inherit from**:

In Python, every class, whether explicitly specified or not, inherits from the base class named `object`. This means that if you define a class without specifying a parent class, it will implicitly inherit from `object`.

The `object` class is the most base type in the Python class hierarchy. It provides a set of default methods to all classes. For instance, methods like `__str__()`, `__repr__()`, and `__eq__()` have their basic definitions in the `object` class.

Here's an example:

```python
class MyClass:
    pass

print(issubclass(MyClass, object))  # Outputs: True
```

Even though `MyClass` does not explicitly inherit from any other class, it is still a subclass of `object`.

Furthermore, when you create a custom class that inherits from another user-defined class, this hierarchy still holds since the parent class, directly or indirectly, eventually inherits from `object`.

For example:

```python
class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))   # Outputs: True
print(issubclass(Child, object))   # Outputs: True
```

In this case, `Child` inherits from `Parent`, and `Parent` inherits from `object`. Hence, `Child` indirectly inherits from `object` as well.

8. **How to override a method or attribute inherited from the base class**:

In object-oriented programming, overriding refers to the ability of a subclass to provide a different implementation for a method that is already defined in its superclass (or an ancestor class). The overridden method in the subclass should have the same name, signature, and parameters as the method in the superclass.

To override a method or attribute inherited from the base class in Python, simply define it in the subclass using the same name.

### Overriding a Method:

Here's a simple example:

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):  # Overriding the 'speak' method of the base class
        return "Woof"

animal = Animal()
print(animal.speak())  # Outputs: Animal sound

dog = Dog()
print(dog.speak())    # Outputs: Woof
```

In this example, the `speak` method in the `Dog` subclass overrides the `speak` method in the `Animal` superclass.

### Overriding an Attribute:

Overriding attributes works in a similar manner. However, be cautious when overriding attributes, as it can lead to unexpected behavior if not done judiciously.

```python
class Parent:
    attribute = "Parent attribute"

class Child(Parent):
    attribute = "Child attribute"  # Overriding the 'attribute' of the base class

parent = Parent()
print(parent.attribute)  # Outputs: Parent attribute

child = Child()
print(child.attribute)  # Outputs: Child attribute
```

### Extending an Overridden Method:

Sometimes, you may want to extend the functionality of a base class method rather than entirely replacing it. In such cases, you can call the base class method using the `super()` function.

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):  # Overriding and extending the 'speak' method
        base_speak = super().speak()  # Call the base class method
        return f"{base_speak}, but specifically Woof for Dog"

dog = Dog()
print(dog.speak())  # Outputs: Animal sound, but specifically Woof for Dog
```

By using the `super()` function, you can ensure that any logic in the superclass method is still executed when the subclass method is called, thereby extending rather than entirely replacing the original functionality.

9. **Which attributes or methods are available by heritage to subclasses**:

When a subclass inherits from a superclass in Python, it gains access to attributes and methods of the superclass. However, the exact attributes and methods available to the subclass depend on several factors:

**Public Attributes and Methods**: All public attributes (variables) and methods (functions) of the superclass are available to the subclass. "Public" means those attributes and methods that do not start with an underscore (`_`). 

**Protected Attributes and Methods**: Attributes and methods that start with a single underscore are conventionally considered "protected" in Python. This is more of a convention rather than enforced by the language. Subclasses can still access these attributes and methods, but the leading underscore suggests that they should be treated as if they are internal to the superclass and should be used cautiously.

**Private Attributes and Methods**: Attributes and methods that start with two underscores (but not ending with two underscores) are considered "private" in Python. This is enforced by name mangling where the interpreter changes the name of the variable to make it harder to access. For instance, an attribute `__my_private_var` in a class `MyClass` would be mangled to `_MyClass__my_private_var`. A subclass can technically still access it using the mangled name, but it's generally considered bad practice to do so.

**Special Methods**: These are methods that start and end with two underscores (e.g., `__init__`, `__str__`, `__eq__`). They are available to subclasses and can be overridden to customize behavior.

**Inherited from `object`**: Every class in Python inherits from the base `object` class, either directly or indirectly. This means that all methods from the `object` class (like `__str__`, `__repr__`, and `__hash__`) are available to all classes, unless overridden.

Here's an example to illustrate:

```python
class SuperClass:
    public_var = "public"
    _protected_var = "protected"
    __private_var = "private"

    def public_method(self):
        return "public method"

    def _protected_method(self):
        return "protected method"

    def __private_method(self):
        return "private method"

class SubClass(SuperClass):
    def show_attributes(self):
        print(self.public_var)        # Accessible
        print(self._protected_var)    # Accessible, but should be used cautiously
        # print(self.__private_var)   # Not directly accessible due to name mangling

    def show_methods(self):
        print(self.public_method())        # Accessible
        print(self._protected_method())    # Accessible, but should be used cautiously
        # print(self.__private_method())   # Not directly accessible due to name mangling

obj = SubClass()
obj.show_attributes()
obj.show_methods()
```

In summary, while subclasses have access to public and protected attributes/methods of the superclass, it's generally recommended to be cautious when accessing or overriding protected members. Private members, due to name mangling, are not directly accessible and should be considered as non-inheritable for most practical purposes.

10. **What is the purpose of inheritance**:

Inheritance is one of the four fundamental principles of object-oriented programming (OOP), alongside encapsulation, polymorphism, and abstraction. The purpose of inheritance includes:

**Reusability**: Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). This reduces redundant code and promotes code reuse. Instead of writing the same code multiple times, common functionalities can be defined in the superclass and then inherited and possibly extended in subclasses.

**Extensibility**: Through inheritance, new classes can be created that are based on existing classes. These new classes can add new attributes and methods or modify the inherited ones to suit specific requirements.

**Logical Hierarchical Structure**: Inheritance helps in creating a natural and logical hierarchical structure for software. For example, in a program about animals, a base class `Animal` can have subclasses like `Bird`, `Mammal`, and `Fish`, and each of these can have further subclasses like `Eagle`, `Dolphin`, etc. This mirrors the kind of categorizations and hierarchies we're familiar with in the real world.

**Polymorphism**: One of the benefits of inheritance is the ability to use a subclass object wherever a superclass object is expected. This is known as polymorphism. It allows for writing more generic and reusable code. For instance, if there's a function that operates on objects of type `Animal`, this function can also accept objects of type `Bird`, `Mammal`, or any other subclass of `Animal`.

**Overriding and Overloading**: Inheritance allows subclasses to provide specific implementations for methods that are already defined in their superclasses. This is known as method overriding. It helps in giving more appropriate functionality to methods in the context of the subclass.

**Maintainability**: With a well-designed inheritance hierarchy, changes made in the superclass can automatically reflect in all subclasses unless overridden. This centralization can make the code easier to maintain and update.

**Establishing Relationships**: Inheritance establishes an "is-a" relationship between the base class and the derived class. For instance, if `Dog` inherits from `Animal`, it establishes that a `Dog` "is-an" `Animal`. This semantic clarity can make the code more intuitive.

While inheritance offers many advantages, it's essential to use it judiciously. Overuse or inappropriate use of inheritance can lead to complex code structures that are hard to maintain and understand. Often, composition (where a class is composed of multiple other classes rather than inheriting from them) is recommended over inheritance for many design scenarios to avoid such complications.

11. **What are, when and how to use isinstance, issubclass, type and super built-in functions**:

**`isinstance(object, classinfo)`**:
   - **Purpose**: This function checks if an object is an instance of a specified class or tuple of classes.
   - **When to use**: You should use `isinstance` when you need to determine if an object is an instance of a particular class or a tuple of classes. It's preferred over using `type` for such checks because it considers subclass relationships.
   - **How to use**:
     ```python
     x = [1, 2, 3]
     if isinstance(x, list):
         print("x is a list")
     ```

**`issubclass(class, classinfo)`**:
   - **Purpose**: This function checks if a class is a subclass of a specified class or tuple of classes.
   - **When to use**: Use `issubclass` when you need to check if one class inherits from another.
   - **How to use**:
     ```python
     class MyBase:
         pass
     
     class MyDerived(MyBase):
         pass
     
     if issubclass(MyDerived, MyBase):
         print("MyDerived is a subclass of MyBase")
     ```

**`type(object)`**:
   - **Purpose**: This function returns the type of an object. When used with one argument, it returns the type of that object.
   - **When to use**: Use `type` when you want to get the direct type of an object, but be aware that it won't consider subclass relationships. For type checking, `isinstance` is often more suitable.
   - **How to use**:
     ```python
     x = [1, 2, 3]
     print(type(x))  # Outputs: <class 'list'>
     ```

**`super([type[, object-or-type]])`**:
   - **Purpose**: This function returns a temporary object of the superclass, allowing you to call its methods. It's primarily used in class inheritance to call methods of the superclass.
   - **When to use**: Use `super` when you need to call a method in a superclass from a derived class. This is especially common in the `__init__` method when initializing a subclass that extends the initialization of a superclass.
   - **How to use**:
     ```python
     class MyBase:
         def __init__(self, value):
             self.value = value
     
     class MyDerived(MyBase):
         def __init__(self, value, extra_value):
             super().__init__(value)  # Calls the __init__ method of MyBase
             self.extra_value = extra_value
     
     obj = MyDerived(10, 20)
     print(obj.value)       # Outputs: 10
     print(obj.extra_value) # Outputs: 20
     ```

To summarize:

- Use `isinstance` for checking if an object is an instance of a class or tuple of classes, considering subclass relationships.
- Use `issubclass` for checking subclass relationships between two classes.
- Use `type` for getting the direct type of an object.
- Use `super` in subclasses when you need to call methods of the superclass, especially during initialization.
