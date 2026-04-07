# # Creating a list of integers
# numbers = [1, 2, 3, 4, 5]
# # Creating a list of strings
# fruits = ["apple", "banana", "cherry"]
# # Creating a list with mixed data types
# mixed_list = [1, "hello", 3.14, True]
# # Creating a list of lists
# nested_list = [[1, 2], [3, 4], [5, 6]]

# # Creating a list using the list() constructor
# numbers = list([1, 2, 3, 4, 5])
# fruits = list(["apple", "banana", "cherry"])
# mixed_list = list([1, "hello", 3.14, True])
# nested_list = list([[1, 2], [3, 4], [5, 6]])

# print(numbers)
# print(fruits)
# print(mixed_list)
# print(nested_list)


# # List element repetation
# # Creating a list with repeated elements
# repeated_list = [0] * 5
# print(repeated_list)

# # Creating a list with repeated strings
# repeated_strings = ["hello"] * 3
# print(repeated_strings)

# # itretion on list

# lst = ["apple", "banana", "cherry"]
# print(lst[2])

# for fruit in lst:
#     print()


# List slicing

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Slicing from index 2 to 5 (exclusive)
# slice1 = lst[2:5]
# print(slice1)  # Output: [3, 4, 5]


# # appending to list
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]

# # extending a list
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# # inserting an element at a specific index
# my_list = [1, 2, 3]
# my_list.insert(1, 10)
# print(my_list)  # Output: [1, 10, 2, 3]

# # removing an element by value
# my_list = [1, 2, 3, 4]
# my_list.remove(2)
# print(my_list)  # Output: [1, 3, 4]

# # removing an element by index
# my_list = [1, 2, 3, 4]
# del my_list[1]
# print(my_list)  # Output: [1, 3, 4]

# # updating an element at a specific index
# my_list = [1, 2, 3]
# my_list[1] = 10
# print(my_list)  # Output: [1, 10, 3]

# # popping an element from the end of the list   
# my_list = [1, 2, 3]
# popped_element = my_list.pop()
# print(popped_element)  # Output: 3
# print(my_list)  # Output: [1, 2]


# sorting a list
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)


# reversing a list
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]
