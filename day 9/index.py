# Goals : 
# Understand what sets are and how they differ from lists/dictionaries
# Learn set operations (union, intersection, difference)
# Discover practical use cases for sets
# Master set methods for common tasks

# Sets are unordered collections of unique elements. sets - no duplicates allowed!
# Mutable: You can add/remove items
# Can contain only immutable types
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

empty_set = set()  # NOT {} - that creates an empty dict!

# From a list with duplicates
colors = ["red", "blue", "red", "green", "blue", "blue"]
unique_colors = set(colors)
print(unique_colors)  # {'red', 'blue', 'green'} - duplicates removed!

# Unordered - may print in different order
print({1, 2, 3} == {3, 2, 1})  # True - order doesn't matter

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Adding and removing
set_a.add(6)        # Add single element
set_a.update({7, 8}) # Add multiple elements
set_a.remove(3)     # Remove element (error if not exists)
set_a.discard(10)   # Remove element (no error if not exists)

print(set_a)

# Two sets of students
math_students = {"Alice", "Bob", "Charlie", "Diana"}
physics_students = {"Charlie", "Diana", "Eve", "Frank"}

# Union: All students in either class
all_students = math_students | physics_students  # OR math_students.union(physics_students)
print(f"All students: {all_students}")

# Intersection: Students in both classes
both_classes = math_students & physics_students  # OR math_students.intersection(physics_students)
print(f"Both classes: {both_classes}")

# Difference: Students only in math
only_math = math_students - physics_students  # OR math_students.difference(physics_students)
print(f"Only math: {only_math}")

# Symmetric Difference: Students in one class but not both
one_class = math_students ^ physics_students  # OR math_students.symmetric_difference(physics_students)
print(f"One class only: {one_class}")