# Python - More Data Structures: Set, Dictionary

# Objectives

## What are sets and how to use them?

Sets are a data type that represent a collection of unique elements. In many programming languages, including Python, sets are provided as a built-in type. Sets are especially useful when you want to keep track of items, and you want to ensure that there are no duplicates.

Here are some key features of sets:

1. **Uniqueness**: Each element in a set is unique. If you try to add an element that already exists, the set will remain unchanged.
2. **Unordered**: Sets are not ordered, so there's no index like with lists or arrays. This means you cannot access an item of a set by an index.
3. **Mutable**: You can add or remove elements from a set, but the elements themselves (if they are of types like lists or dictionaries) cannot be modified directly once they are inside the set.

### Common operations with sets:

- **Creation**: You can create a set using curly braces `{}` or the `set()` function.
- **Add elements**: Use the `add()` method.
- **Remove elements**: Use the `remove()` or `discard()` methods.
- **Union**: Use the `|` operator or the `union()` method.
- **Intersection**: Use the `&` operator or the `intersection()` method.
- **Difference**: Use the `-` operator or the `difference()` method.

### Examples in Python:

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
colors = set(["red", "green", "blue"])

# Adding an element
fruits.add("orange")

# Removing an element (raises an error if the element is not present)
fruits.remove("banana")

# Removing an element (does not raise an error if the element is not present)
fruits.discard("banana")

# Union of sets
all_items = fruits | colors

# Intersection of sets
common = fruits & colors

# Difference of sets
diff = fruits - colors
```

### Use Cases:

1. **Eliminating Duplicates**: Convert a list to a set and back to a list to remove duplicates.
2. **Membership Test**: Check if an element is present in a collection.
3. **Set Arithmetic**: Identify common elements or differences between collections.
4. **Data Analysis**: In tasks like filtering out unique items from large datasets.

While sets are powerful, they're not always the right choice. For example, if order matters or if you want to store non-unique items, a list or another data type might be more appropriate.

