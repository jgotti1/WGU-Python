# Multiple key-value pairs, each representing a person's name and age, are read from input and added to patients_info. Output each key in patients_info in sorted order, with each key on a new line.

# Click here for example
# Ex: If the input is:
# Zoe 29
# Val 13
# end

# then the output is:

# Val
# Zoe

patients_info = {}

input_line = input()
while input_line != 'end':
    name, age = input_line.split()
    patients_info[name] = int(age)
    input_line = input()

sorted_list = list(patients_info.keys())

sorted_list.sort()

for name in sorted_list:
  print(name)
