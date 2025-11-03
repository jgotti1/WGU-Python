# List trend_line contains integers read from input, representing an increasing sequence of data values. minimum_diff measures the minimum difference between two neighboring values in the sequence, and is initialized with None. For each index i of trend_line from 1 through the last index:

# Compute variable neighbor_diff as the element at index i minus the element at index i - 1.
# Output the element at index i, followed by ' - ', the element at index i - 1, ' = ', and the value of neighbor_diff.
# Assign minimum_diff with the minimum value of neighbor_diff computed in all the iterations.

# Click here for example
# Ex: If the input is 15 22 30 31 40, then the output is:
# Sequence: [15, 22, 30, 31, 40]
# 22 - 15 = 7
# 30 - 22 = 8
# 31 - 30 = 1
# 40 - 31 = 9
# The minimum difference between two neighboring values is 1
# Note: trend_line always has at least two elements.

# Read input and split input into tokens
tokens = input().split()

trend_line = []
for token in tokens:
    trend_line.append(int(token))

print(f'Sequence: {trend_line}')

minimum_diff = None
neighbor_diff = 0

for pos, value in enumerate(trend_line[:-1]):
  
  neighbor_diff = trend_line[pos+1] - value
  print (f'{trend_line[pos + 1]} - {value} = {neighbor_diff}')
  
  if minimum_diff == None:
    minimum_diff = 0
    
  if neighbor_diff < minimum_diff or minimum_diff == 0:
    minimum_diff = neighbor_diff

print(f'The minimum difference between two neighboring values is {minimum_diff}')