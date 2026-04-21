# What is Sets in Python?

## A set is an unordered collection of unique elements. It is a built-in data type in Python that allows you to store and manipulate a collection of items without any particular order. Sets are defined using curly braces `{}` or the `set()` constructor.

## Key features of sets in Python:
1. **Unordered**: The elements in a set do not have a specific order, and you cannot access them using an index.
2. **Unique**: A set cannot contain duplicate elements. If you try to add a duplicate element, it will be ignored.
3. **Mutable**: You can add or remove elements from a set after it has been created.

## Creating a Set
You can create a set using curly braces `{}` or the `set()` constructor. Here are some examples:

```python
# Using curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Using the set() constructor
another_set = set([1, 2, 3, 4, 5])
print(another_set)  # Output: {1, 2, 3, 4, 5}
```

## Adding and Removing Elements
You can add elements to a set using the `add()` method and remove elements using the `remove()` or `discard()` methods.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}
my_set.discard(3)
print(my_set)  # Output: {1, 4}
```
## Set Operations
Sets support various operations such as union, intersection, difference, and symmetric difference. Here are some examples:

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# Symmetric Difference
sym_diff_set = set_a.symmetric_difference(set_b)
print(sym_diff_set)  # Output: {1, 2, 4, 5}
```

## List of methsods in sets:
- `add()`: Adds an element to the set.
- `remove()`: Removes an element from the set. Raises a KeyError if the element is not found.
- `discard()`: Removes an element from the set if it is present. Does nothing if the element is not found.
- `union()`: Returns a new set that is the union of two sets.
- `intersection()`: Returns a new set that is the intersection of two sets.
- `difference()`: Returns a new set that is the difference of two sets.
- `symmetric_difference()`: Returns a new set that is the symmetric difference of two sets.
- `clear()`: Removes all elements from the set.
- `copy()`: Returns a shallow copy of the set.
- `isdisjoint()`: Returns True if two sets have no elements in common.
- `issubset()`: Returns True if the set is a subset of another set.
- `issuperset()`: Returns True if the set is a superset of another set
- `pop()`: Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
- `len()`: Returns the number of elements in the set.
- `in`: Checks if an element is in the set.