# 9.20.1: LAB: Filter and sort a list

# Full screen
# 0 / 10
# Write a program that gets a list of integers from input, and outputs negative integers in descending order (highest to lowest).

# Ex: If the input is:

# 10 -7 4 -39 -6 12 -2
# the output is:

# -2 -6 -7 -39 

my_list = [int(num) for num in input().split() if int(num) < 0]
# for num in my_list:
#   if num >= 0:
#     my_list.remove(num)
    
my_list.sort(reverse=True)

print(" ".join(str(n) for n in my_list), end="")
