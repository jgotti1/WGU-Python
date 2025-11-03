# List bacteria_colonies contains integers read from input. Each integer represents a random data sample in an experiment. Write a loop to update all the elements at odd-numbered indices in bacteria_colonies with 0.

# Click here for example
# Ex: If the input is 80 12 96 22, then the output is:

# Original samples: 80 12 96 22 
# Reduced samples: 80 0 96 0 

bacteria_colonies = []

tokens = input().split()
for token in tokens:
    bacteria_colonies.append(int(token))
  
print('Original samples:', end=' ')
for sample in bacteria_colonies:
    print(sample, end=' ')
print()

for index, value in enumerate(bacteria_colonies):
  if index % 2 != 0:
    bacteria_colonies[index] = 0
    

print('Reduced samples:', end=' ')
for sample in bacteria_colonies:
    print(sample, end=' ')
print()