# What is List?

1. list is a built-in data structure in Python that is used to store an ordered collection of items. It is one of the most versatile and commonly used data structures in Python.

2. list is ordered, mutable, and allows duplicate elements. 

3. list is defined using square brackets `[]` and can contain elements of different data types, including other lists.

4. we can also define a list using the `list()` constructor, which can take an iterable as an argument. For example:

# Creating a List

You can create a list by enclosing a comma-separated sequence of items in square brackets. Here are some examples:

```python
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]
# Creating a list of strings
fruits = ["apple", "banana", "cherry"]
# Creating a list with mixed data types
mixed_list = [1, "hello", 3.14, True]
# Creating a list of lists
nested_list = [[1, 2], [3, 4], [5, 6]]

# Creating a list using the list() constructor
numbers = list([1, 2, 3, 4, 5])
fruits = list(["apple", "banana", "cherry"])
mixed_list = list([1, "hello", 3.14, True])
nested_list = list([[1, 2], [3, 4], [5, 6]])
```


# Methods of List
Python lists have a variety of built-in methods that allow you to manipulate and work with the list data structure. Here are some commonly used list methods:
1. `append()`: Adds an item to the end of the list.
2. `extend()`: Extends the list by appending elements from another iterable.
3. `insert()`: Inserts an item at a specified index.
4. `remove()`: Removes the first occurrence of a specified value.
5. `pop()`: Removes and returns the item at a specified index (default is the last item).
6. `clear()`: Removes all items from the list.
7. `index()`: Returns the index of the first occurrence of a specified value.
8. `count()`: Returns the number of occurrences of a specified value.
9. `sort()`: Sorts the items of the list in place.
10. `reverse()`: Reverses the order of the items in the list.
11. `copy()`: Returns a shallow copy of the list.
Here are some examples of how to use these methods:

```python
# Creating a list
my_list = [1, 2, 3]
# Using append() to add an item to the end of the list
my_list.append(4)  # my_list is now [1, 2,3, 4]
# Using extend() to add multiple items to the list
my_list.extend([5, 6])  # my_list is now [1, 2, 3, 4, 5, 6]
# Using insert() to add an item at a specific index
my_list.insert(0, 0)  # my_list is now [0, 1, 2, 3, 4, 5, 6]
# Using remove() to remove the first occurrence of a value
my_list.remove(3)  # my_list is now [0, 1, 2, 4, 5, 6]
# Using pop() to remove and return an item at a specific index
popped_item = my_list.pop(2)  # popped_item is 2, my_list is now [0, 1, 4, 5, 6]
# Using clear() to remove all items from the list
my_list.clear()  # my_list is now []
# Using index() to find the index of a value    
my_list = [1, 2, 3, 4, 5]
index_of_3 = my_list.index(3)  # index_of_3 is 2
# Using count() to count occurrences of a value
my_list = [1, 2, 2, 3, 4]
count_of_2 = my_list.count(2)  # count_of_2 is 2
# Using sort() to sort the list in place
my_list.sort()  # my_list is now [1, 2, 2, 3, 4]
# Using reverse() to reverse the order of the list  
my_list.reverse()  # my_list is now [4, 3, 2, 2, 1]
# Using copy() to create a shallow copy of the list
my_list_copy = my_list.copy()  # my_list_copy is [4, 3, 2, 2, 1]
``` 