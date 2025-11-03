# Write a program that first gets a list of integers from input. That list is followed by two more integers representing lower and upper bounds of a range. Your program should output all integers from the list that are within that range (inclusive of the bounds).

# Ex: If the input is:

# 25 51 0 200 33
# 0 50
# the output is:

# 25,0,33,
# The bounds are 0-50, so 51 and 200 are out of range and thus not output.

# For coding simplicity, follow each output integer by a comma, even the last one. Do not end with newline.

my_list1 = [int(x) for x in input().split()]
bounds = [int(x) for x in input().split()]

new_list = []

for n in my_list1:
  if n >= bounds[0] and n <= bounds[1]:
    new_list.append(n)

print(",".join(str(n) for n in new_list), end=",")





