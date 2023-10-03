# Python - Data Structures: Lists, Tuples

# Objectives
## What are lists and how to use them?
## What are the differences and similarities between strings and lists?
## What are the most common methods of lists and how to use them?
## How to use lists as stacks and queues?
## What are list comprehensions and how to use them?
## What are tuples and how to use them?
## When to use tuples versus lists?
## What is a sequence?
## What is tuple packing?
## What is sequence unpacking?
## What is the del statement and how to use it?

1. **What are lists and how to use them?**
    - Lists in Python are a collection data type that can hold multiple items in an ordered sequence. Lists are mutable, which means their elements can be changed after they are created.
    - Usage: `my_list = [1, 2, 3, 'a', 'b']`

2. **Differences and similarities between strings and lists:**
    - **Similarities:**
        - Both can be indexed and sliced.
        - Both are iterable.
    - **Differences:**
        - Strings are immutable, whereas lists are mutable.
        - Lists can hold any data type, including other lists; strings only hold characters.

3. **Most common methods of lists and how to use them:**
    - `append(item)`: Adds an item to the end.
    - `extend(iterable)`: Adds all elements of an iterable to the list.
    - `insert(index, item)`: Inserts item at a specific position.
    - `remove(item)`: Removes first occurrence of item.
    - `pop(index)`: Removes item at the specified index and returns it.
    - `index(item)`: Returns the index of the first occurrence of an item.
    - `count(item)`: Returns the count of how many times an item appears.
    - `sort()`: Sorts the list in place.
    - `reverse()`: Reverses the list in place.

4. **Using lists as stacks and queues:**
    - **Stack**: LIFO (Last In, First Out). Use `append()` to push and `pop()` to pop.
    - **Queue**: FIFO (First In, First Out). It's inefficient to use lists directly as queues due to shifts in elements. Instead, use `collections.deque`.

5. **List comprehensions and how to use them:**
    - A concise way to create lists.
    - Example: `[x**2 for x in range(10) if x % 2 == 0]` creates a list of squares for even numbers up to 10.

6. **Tuples and how to use them:**
    - Like lists, but immutable.
    - Usage: `my_tuple = (1, 2, 3)`

7. **When to use tuples vs lists:**
    - Use tuples for heterogeneous data and when immutability is needed.
    - Use lists when you need a mutable sequence.

8. **What is a sequence?**
    - A sequence is an ordered collection of items. Strings, lists, and tuples are all sequences.

9. **Tuple packing:**
    - Automatically packing values into a tuple.
    - Example: `t = 1, 2, 3`

10. **Sequence unpacking:**
    - Assigning individual elements of a sequence to multiple variables.
    - Example: `x, y, z = t`

11. **The `del` statement and its usage:**
    - Used to delete items, slices, or entire lists.
    - Example:
        ```python
        my_list = [1, 2, 3]
        del my_list[1]  # Removes the second item
        ```

I hope this gives you a solid understanding of the topics you've listed! If you want to dive deeper into any of these topics, please let me know!
