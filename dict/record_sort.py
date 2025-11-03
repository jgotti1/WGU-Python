# Multiple key-value pairs, each representing a person's name and age, are read from input and added to patients_record. Convert patients_record's keys into a list and then sort the list. Assign sorted_keys with the sorted list.

# Click here for example
# Ex: If the input is:
# Del 82
# Ana 51
# end

# then the output is:

# ['Ana', 'Del']

patients_record = {}

input_line = input()
while input_line != 'end':
    name, age = input_line.split()
    patients_record[name] = int(age)
    input_line = input()
    
# print(patients_record)
    
sorted_keys = list(patients_record.keys())
    
sorted_keys.sort()

print(sorted_keys)