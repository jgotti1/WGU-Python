
# Integers initial_value and final_value are read from input. 
# For each number from initial_value to final_value both inclusive, output the number's value of hashtag characters ('#').

# Ex: If the input is:
# 3
# 4
# then the output is:

# ###
# ####
# Note: print(x, end='') outputs x without ending with a default newline.

initial_value = int(input())
final_value = int(input())

for i in range(initial_value, final_value + 1):
    for p in range(i):
      print("#", end='')
    print()
    