# String manipulation
print("\nString Methods")
print("=" * 20)

text = "  python programming  "

print(f"Original: '{text}'")
print(f"Upper case: {text.upper()}")
print(f"Lower case: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Stripped: '{text.strip()}'")  # Removes spaces
print(f"Replace: {text.replace('python', 'Python')}")

# String checking methods
email = "student@email.com"
print(f"\nEmail validation:")
print(f"Starts with st: {email.startswith('st')}")
print(f"Ends with .com: {email.endswith('.com')}")
print(f"Contains @: {'@' in email}")
print(f"Is alphabetic: {'python'.isalpha()}")

# Lists are ordered, changeable collections.
# like a shopping list that we can modify.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"  # Change item
fruits.append("kiwi")  # Add item
fruits.remove("banana")  # Remove item
fruits.pop()  # Remove last item
fruits.insert(1, "grape")  # Insert at index
fruits.sort()  # Sort items
print(f"\nFruits List: {fruits}")


# Tuples are ordered but unchangeable.
# Once created, we can't modify them.
example1 = (1,)
colors = ("red", "green", "blue")
# colors[0] = "yellow"  # This will raise an error
print(type(example1))  # This is a tuple


