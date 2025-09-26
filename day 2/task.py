# Create a file called calculate.py.
# Write a program that:

# Asks the user for two numbers.
num_one = int(input("Enter first num: "))
num_two = int(input("Enter second num: "))

# Calculates and displays the sum, difference, product, and quotient of those numbers.
sum_of_nums = num_one + num_two
print("num_1 + num_2 = ", sum_of_nums)

diff_of_nums = num_one - num_two
print("num_1 - num_2 = ", diff_of_nums)

product_of_nums = num_one * num_two
print("num_1 * num_2 = ", product_of_nums)

quot_nums = num_one % num_two
print("num_1 % num_2 = ", quot_nums)
# Shows whether the first number is greater than the second.
does_it_greater = num_one > num_two
print(does_it_greater)
