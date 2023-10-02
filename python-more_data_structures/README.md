# Python - More Data Structures: Set, Dictionary

# Objectives

====================================================================================================================================================

## What are sets and how to use them?
## What are the most common methods of set and how to use them?
## How to iterate into a set?

A set is an unordered collection of unique elements. They are similar to lists and tuples, but unlike these sequences, sets cannot have multiple occurrences of the same element. This makes sets highly useful in many scenarios where you need to ensure the uniqueness of elements. Sets in Python are mutable, meaning, you can add or remove items after the set is created.

### How to Use Sets:

#### Creating a Set:

```python
# Using curly braces
my_set = {1, 2, 3, 4}

# Using the set() function
another_set = set([1, 2, 3, 4])
```

#### Adding Elements:

```python
my_set.add(5)  # my_set is now {1, 2, 3, 4, 5}
```

#### Removing Elements:

```python
my_set.remove(5)  # my_set is now {1, 2, 3, 4}
```

#### Discarding Elements:

```python
my_set.discard(5)  # No error if the element is not present
```

### Common Set Methods:

1. `add(element)`: Adds an element to the set.
2. `remove(element)`: Removes the element from the set. Raises an error if the element is not present.
3. `discard(element)`: Removes the element from the set if it's present. Does not raise an error otherwise.
4. `pop()`: Removes and returns an arbitrary element from the set. Raises an error if the set is empty.
5. `clear()`: Removes all elements from the set.
6. `union(set)`: Returns a set containing all elements from the original set and the specified set(s). Can also use the `|` operator.
7. `intersection(set)`: Returns a set containing only elements found in both the original set and the specified set(s). Can also use the `&` operator.
8. `difference(set)`: Returns a set containing elements in the original set that aren't in the specified set(s). Can also use the `-` operator.
9. `symmetric_difference(set)`: Returns a set containing elements that are in either of the sets, but not in both. Can also use the `^` operator.
10. `issubset(set)`: Returns `True` if all elements of the original set are present in the specified set.
11. `issuperset(set)`: Returns `True` if all elements of the specified set are present in the original set.
12. `isdisjoint(set)`: Returns `True` if no elements are shared between the original set and the specified set.

### Iterating over a Set:

Since sets are iterable, you can use a simple `for` loop to iterate over its elements:

```python
my_set = {1, 2, 3, 4}

for element in my_set:
    print(element)
```

Remember, since sets are unordered, the order of elements when iterating might not be what you expect.

## Note:

One key thing to keep in mind is that sets are collections of hashable (or immutable) items. This means you can't include lists or dictionaries as set elements, but you can include tuples.

====================================================================================================================================================

## When to use sets versus lists?

Both sets and lists are fundamental data structures in Python, and while they can sometimes be used interchangeably, each has its strengths and ideal use cases. Here's a breakdown of when to use one over the other:

## When to use sets:

1. **Uniqueness:** If you want to automatically ensure all elements are unique, then use a set. Duplicates are automatically removed.

   ```python
   numbers = {1, 2, 2, 3, 4, 4, 4}
   # numbers is now {1, 2, 3, 4}
   ```

2. **Membership Testing:** Checking if an item exists in a set is generally faster than checking if an item exists in a list, especially as the number of elements grows.

   ```python
   if value in my_set:
       # do something
   ```

3. **Set Operations:** If you need to perform operations like union, intersection, difference, etc., sets provide built-in methods and operators for these.

   ```python
   a = {1, 2, 3, 4}
   b = {3, 4, 5, 6}
   union = a | b  # {1, 2, 3, 4, 5, 6}
   ```

4. **Removing Duplicates:** If you have a list and you want to remove duplicates quickly, converting it into a set and back to a list is a common trick:

   ```python
   my_list = [1, 2, 2, 3, 4, 4, 4]
   my_list = list(set(my_list))
   ```

## When to use lists:

1. **Order Matters:** Lists maintain the order of elements. If the order in which items are added or arranged is crucial, you should use a list.

2. **Duplicate Values:** If you need to store duplicate values, lists allow for this.

3. **Indexing:** If you need to fetch an item based on its position or index, or modify items based on their position, lists provide this functionality.

   ```python
   first_element = my_list[0]
   ```

4. **Slice Notation:** Lists support slicing which is useful for fetching or modifying ranges of items.

   ```python
   sublist = my_list[1:4]
   ```

5. **Appending or Extending:** Lists offer methods like `append()`, `extend()`, and `insert()` which can be handy if you frequently need to add items.

6. **More Built-in Methods:** Lists offer methods like `count()`, `index()`, `reverse()`, and `sort()`. Some of these methods, like `sort()`, don't have direct analogs with sets since sets are unordered.

## Conclusion:

While both sets and lists have overlapping capabilities, your choice should largely depend on your specific needs:

- If you're dealing with unique values, membership tests, or set operations, opt for a set.
- If order, indexing, or duplication is essential, a list is the way to go.

====================================================================================================================================================

## What are dictionaries and how to use them?
## What is a key in a dictionary?
## How to iterate over a dictionary?

Dictionaries (`dict` in Python) are mutable, unordered collections of items. Each item is stored as a key-value pair. Keys in a dictionary are unique, which means there can be no two items with the same key in a dictionary. This makes dictionaries incredibly efficient for lookups based on the key.

### How to Use Dictionaries:

#### Creating a Dictionary:

```python
# Using curly braces
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using the dict() function
another_person = dict(name="Jane", age=25, city="Los Angeles")
```

#### Accessing Values:

```python
print(person["name"])  # Outputs: John

# Using the get() method which provides a way to set a default value if the key doesn't exist
print(person.get("country", "USA"))  # Outputs: USA
```

#### Modifying/Adding Items:

```python
person["age"] = 31  # Modifies the age
person["country"] = "USA"  # Adds a new key-value pair
```

#### Removing Items:

```python
del person["age"]  # Removes the key "age" and its associated value

# Using the pop() method
person.pop("city")  # Removes the key "city" and returns its value
```

### What is a Key in a Dictionary?

A key in a dictionary is a unique identifier used to access its corresponding value. The key is the part before the colon (`:`) in a key-value pair, and the value is the part after. Keys in dictionaries must be of a hashable data type, like numbers, strings, or tuples. Lists, for example, cannot be used as dictionary keys because they are mutable and unhashable.

### How to Iterate Over a Dictionary:

Dictionaries can be iterated in several ways:

1. **Iterating Over Keys:**

   ```python
   for key in person:
       print(key)
   ```

   OR

   ```python
   for key in person.keys():
       print(key)
   ```

2. **Iterating Over Values:**

   ```python
   for value in person.values():
       print(value)
   ```

3. **Iterating Over Key-Value Pairs:**

   ```python
   for key, value in person.items():
       print(key, value)
   ```

In these examples, `person.keys()` returns a list-like view of the keys, `person.values()` returns a view of the values, and `person.items()` returns a view of the key-value pairs as tuples.

Do note that the order of items in a dictionary was arbitrary prior to Python 3.7. However, from Python 3.7 onwards, dictionaries maintain the order of items based on their insertion order, so the above iteration methods will reflect this order.

====================================================================================================================================================

## When to use dictionaries versus lists or sets?

Lists, sets, and dictionaries are among the most commonly used data structures in Python. Deciding when to use each can be based on their characteristics and typical use-cases:

## When to Use Dictionaries:

1. **Key-Value Pair Storage:** If you have data that can be naturally structured as key-value pairs, dictionaries are the go-to choice. For example, if you're storing attributes of a person (name, age, address), using a dictionary is intuitive.

   ```python
   person = {"name": "John", "age": 30, "address": "123 Main St"}
   ```

2. **Fast Lookups by Key:** Dictionaries are implemented as hash tables, which means they offer very fast O(1) lookups by key. If you need to quickly access a value based on a unique identifier (key), a dictionary is optimal.

3. **Data with Unique Identifiers:** When each piece of data can be identified by a unique key, dictionaries are an appropriate choice.

## When to Use Lists:

1. **Ordered Collection:** When the order of elements matters, use a list. Lists maintain the order of elements based on their insertion.

2. **Index-Based Access:** If you need to fetch or modify items based on their position or want to easily slice subsets of your data, lists are the way to go.

3. **Duplicates Allowed:** When your data can have duplicate values, lists are suitable.

4. **Iterating in Sequence:** If you need to process items in the order they were added, or if the order of processing matters, a list is preferable.

## When to Use Sets:

1. **Unique Elements:** If you need to ensure all elements are unique, sets are the most suitable.

2. **Fast Membership Tests:** Sets offer O(1) average time complexity for membership tests (e.g., `if x in my_set`). This is faster than lists, especially for larger collections.

3. **Set Operations:** For operations like union, intersection, difference, etc., sets provide built-in methods.

4. **Removing Duplicates:** If you have a list and want to deduplicate it quickly, converting it into a set and back to a list is a common approach.

5. **Unordered Data:** If the order of elements does not matter for your use case, and you need uniqueness, sets are ideal.

## Conclusion:

- Use **dictionaries** when dealing with data that can be mapped as unique keys to values, especially when you need to look up values by their keys rapidly.
  
- Use **lists** when the order of elements matters, when you need to access elements by their position, or when duplicates are permissible.

- Use **sets** when you need to ensure elements are unique, when you want to perform set operations, or when you need fast membership testing without concern for the order of elements. 

Understanding the strengths and limitations of each data structure will help you make the right choice for a given scenario.

====================================================================================================================================================

# What is a lambda function?
# What are the map, reduce and filter functions?

## Lambda Function

A `lambda` function is a small, anonymous function in Python. It can take any number of arguments, but can only have one expression. The expression is evaluated and returned when the lambda function is called. Lambda functions are used primarily when you need a simple function for a short period and do not want to formally define it using the `def` keyword.

**Syntax:**

```python
lambda arguments: expression
```

**Example:**

```python
f = lambda x: x * x
print(f(7))  # Outputs: 49
```

## Map Function

The `map()` function applies a given function to all items in an input list (or any other iterable). It returns an iterable map object, which can be converted into a list or another iterable type.

**Syntax:**

```python
map(function, iterable, ...)
```

**Example:**

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Outputs: [1, 4, 9, 16]
```

## Filter Function

The `filter()` function constructs a list (or another iterable) from elements of an iterable for which a function returns `True`. In simple words, it filters the elements based on a function.

**Syntax:**

```python
filter(function, iterable)
```

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Outputs: [2, 4]
```

## Reduce Function

The `reduce()` function is part of the `functools` module in Python 3 (in Python 2, it was a built-in function). It continuously applies a function to the elements of an iterable, from left to right, so as to reduce the iterable to a single cumulative value.

**Syntax:**

```python
functools.reduce(function, iterable[, initializer])
```

If the initializer is present, it's placed before the items of the iterable in the computation, and serves as a default when the iterable is empty.

**Example:**

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Outputs: 24 (which is 1*2*3*4)
```

In this example, the `reduce()` function multiplies all elements of the list together.

## In Summary:

- `lambda`: A way to create small, anonymous functions.
  
- `map()`: Apply a function to every item of an iterable.
  
- `filter()`: Filter items out of an iterable.
  
- `reduce()`: Reduce an iterable to a single cumulative value by applying a binary function.

====================================================================================================================================================
