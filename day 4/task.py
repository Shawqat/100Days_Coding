# Create a file called loop_practice.py.
# Write a program that:
# Prints numbers from 1 to 10 using a for loop.
# Prints even numbers from 1 to 20 using a while loop.
# Loops through a list of your favorite foods and prints each one.
# Sample Output:
# 1
# 2
# 3
# ...
# 10

# 2
# 4
# 6
# ...
# 20

# Pizza
# Burger
# Sushi
# ...

# Prints numbers from 1 to 10
# for number in range(1,11):
#     print(number)

# print("#" * 10)

# Prints even numbers from 1 to 20
# counter = 2
# while counter <= 20:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1

# Loops through a list of your favorite foods and prints each one.
# favorite_foods = ["Pizza", "Burger", "Sushi"]
# for item in favorite_foods:
#     print(item)

# Challenge : Use a loop to calculate the sum of all numbers from 1 to 100 and print the result.

all_numbers = 0
for number in range(1,101):
    all_numbers += number

print("result =", all_numbers)