# List measurements_list contains integers read from input, representing data samples from an experiment. For each element in measurements_list:

# If the element's value is less than or equal to 65, then output 'Sample ', followed by the element's index, and ' is accepted'.
# Otherwise, increment count_dropped and output 'Sample ', followed by the element's index, and ' is dropped'.
# Click here for example
# Ex: If the input is 64 66 73 65, then the output is:
# Raw samples: [64, 66, 73, 65]
# Sample 0 is accepted
# Sample 1 is dropped
# Sample 2 is dropped
# Sample 3 is accepted
# Total dropped samples: 2

# Read input and split input into tokens
tokens = input().split()

measurements_list = []
for token in tokens:
    measurements_list.append(int(token))

print(f'Raw samples: {measurements_list}')

count_dropped = 0

for pos, value in enumerate(measurements_list):
    if value <= 65:
        print(f'Sample {pos} is accepted')
    else:
        count_dropped += 1
        print(f'Sample {pos} is dropped')

print(f'Total dropped samples: {count_dropped}')