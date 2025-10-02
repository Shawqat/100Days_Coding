# Goals:
# Understand what dictionaries are and how they work
# Learn to create, access, and manipulate dictionaries
# Discover practical use cases for dictionaries
# Master essential dictionary methods

# Creating dictionaries
# student = {
#     "name": "Mahmoud",
#     "age": 27,
#     "major": "Nursing",
#     "gpa": 3.8
# }

# Alternative ways to create dictionaries
# colors = dict(red="#FF0000", green="#00FF00", blue="#0000FF")
# empty_dict = {}

# print(f"Iam {student["name"]}, and Iam {student["age"]} years old.")
# Using get() - safer, won't crash if key doesn't exist
# print(f"{student.get("gpa","N/A")}")
# print(f"{student.get("city","Egypt, Cairo")}")

#  Adding new key-value pairs
# student["email"] = "Mo@university.edu"

# Modifying existing values
# student["age"] = 24

# Removing items
# removed_value = student.pop("emaol")  # Remove and return value
# del student["gpa"]  # Remove without returning

# print(student)

inventory = {"apples": 10, "bananas": 5, "oranges": 8}

# Get all keys, values, or key-value pairs
print(inventory.keys())    # dict_keys(['apples', 'bananas', 'oranges'])
print(inventory.values())  # dict_values([10, 5, 8])
# dict_items([('apples', 10), ('bananas', 5), ('oranges', 8)]),
# list of tuples
print(inventory.items())   

# Check if key exists
print("apples" in inventory)  # True
print("grapes" in inventory)  # False

# Update dictionary
inventory.update({"bananas": 7, "grapes": 15})  # Update existing, add new

# nesting dictionaries

students = {
    "001": {"name": "Alice", "age": 20, "major":" Computer Science"},
    "002": {"name": "Bob", "age": 22, "major":"Mathematics"},
}

# Access nested value, and same for update, delete
print(students["001"]["name"]) 