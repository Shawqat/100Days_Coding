# A function lets you group code together to perform a specific task.
# It helps make your code reusable and easier to read.

def greet(name):
    print("Hello,", name)

greet("Shawqat")  # Output: Hello, Shawqat

# Functions can take inputs (parameters) and return outputs (using return).
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8

# Error handling is important to prevent your program from crashing if something goes wrong.
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That's not a valid number!")
