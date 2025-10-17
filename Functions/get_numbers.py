# zyDE 7.7.1: User-defined functions make a program easier to understand.
# The problem below uses the function get_numbers() to read a number of integers from the user. Three unfinished functions are defined, which should print only certain types of numbers that the user entered. Complete the unfinished functions, adding loops and branches where necessary. Match the output with the below sample:


size = 5
neg_numbers = []
odd_numbers=[]

def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers: ', *numbers)

def print_odd_numbers(numbers):
  
  for odd in numbers:
    if odd % 2 != 0:
      odd_numbers.append(odd)
    else:
      continue

    # Print all odd numbers


def print_negative_numbers(numbers):
   
   for neg in numbers:
    if neg < 0:
      neg_numbers.append(neg)
    else:
      continue
    # Print all negative numbers


nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
print('Odd numbers:', *odd_numbers)
print('Negative numbers:', *neg_numbers)