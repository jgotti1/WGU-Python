# List data_list contains integers read from input, representing data samples from an experiment. Initialize variable sum_accepted with 0. Then, for each element in data_list that is both at an odd-numbered index and greater than or equal to 55:

# Output 'Sample at index ', followed by the element's index, ' is ', and the element's value.
# Increase sum_accepted by each such element's value.
# Click here for example
# Ex: If the input is 67 55 56 54 18 17, then the output is:
# All data: [67, 55, 56, 54, 18, 17]
# Sample at index 1 is 55
# Sum of selected elements is: 55

# Read input and split input into tokens
tokens = input().split()

data_list = []
for token in tokens:
    data_list.append(int(token))

print(f'All data: {data_list}')

sum_accepted = 0

for pos, value in enumerate(data_list):
  if (pos % 2 != 0) and value >= 55:
    print(f'Sample at index {pos} is {value}')
    sum_accepted = value + sum_accepted

    
    

print(f'Sum of selected elements is: {sum_accepted}')