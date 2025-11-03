# Statistics are often calculated with varying amounts of input data. Write a program that takes any number of non-negative floating-point numbers as input, and outputs the max and average, respectively.

# Output the max and average with two digits after the decimal point.

# Ex: If the input is:

# 14.25 25 0 5.75
# the output is:

# 25.00 11.25

my_numbers = [float(n) for n in input(f"Enter your numbers: ").split()]

average = sum(my_numbers) / len(my_numbers)
max  = max(my_numbers)

print(f'{max:.2f} {average:.2f}')