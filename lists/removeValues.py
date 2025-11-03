# List data_samples contains integers read from input. Each integer represents a random data sample in an experiment. Write a loop to remove every element from data_samples that is less than 35 and output the removed element, followed by ' dropped'.

# Click here for example
# Ex: If the input is 44 14 16 35, then the output is:

# Original samples: 44 14 16 35 
# 14 dropped
# 16 dropped
# Filtered samples: 44 35 


data_samples = []

tokens = input().split()
for token in tokens:
    data_samples.append(int(token))
  
print('Original samples:', end=' ')
for samples in data_samples:
    print(samples, end=' ')
print()

for value in data_samples[:]:
  if value < 35:
    print(f'{value} dropped')
    data_samples.remove(value)

print('Filtered samples:', end=' ')
for samples in data_samples:
    print(samples, end=' ')
print()