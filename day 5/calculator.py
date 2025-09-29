# function for sum
def add(num1, num2):
    return num1 + num2

# function for difference
def subtract(num1, num2):
    return num1 - num2  # Returns signed difference

# function for product
def multiply(num1, num2):
    return num1 * num2

# function for division
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Don't use zero!"

status = input("Do you want to start the calculator? (yes/no): ")
while status.lower() == "yes":
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers!")
        continue

    operation = input("Choose operation (+, -, *, /) or type 'exit' to quit: ")
    if operation == "+":
        print("Result:", add(number1, number2))
    elif operation == "-":
        print("Result:", subtract(number1, number2))
    elif operation == "*":
        print("Result:", multiply(number1, number2))
    elif operation == "/":
        print("Result:", divide(number1, number2))
    elif operation.lower() == "exit":
        print("Exiting calculator.")
        break
    else:
        print("Not a valid operation!")

    status = input("Do you still want to continue? (yes/no): ")