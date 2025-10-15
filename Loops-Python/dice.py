# The following is a sample programming lab activity; not all classes using a zyBook require students to fully complete this activity. No auto-checking is performed. Students planning to fully complete this program may consider first developing their code in a separate programming environment.

# Analyzing dice rolls is a frequent example in understanding probability and statistics. The following program calculates the number of times the sum of two dice (randomly rolled) is equal to six or seven.


# Create a different version of the program that:

# calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.
# repeatedly asks the user for the number of times to roll the dice, quitting only when the user-entered number is less than 1. Hint: Use a while loop that will execute as long as num_rolls is greater than or equal to 1.
# prints a histogram in which the total number of times the dice rolls equals each possible value and is displayed by printing a character, such as *, that number of times. Ex:

import random

num_twos = 0
num_threes = 0
num_fours = 0
num_fives = 0
num_sixes = 0
num_sevens = 0
num_eights = 0
num_nines = 0
num_tens = 0
num_elevens = 0
num_twelves = 0

num_rolls = int(input('Enter number of rolls:\n'))


i = 1
while i <= num_rolls:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll_total = die1 + die2
    i += 1

  # Check which total it is and increment that counter
    if roll_total == 2:
        num_twos += 1
    elif roll_total == 3:
        num_threes += 1
    elif roll_total == 4:
        num_fours += 1
    elif roll_total == 5:
        num_fives += 1
    elif roll_total == 6:
        num_sixes += 1
    elif roll_total == 7:
        num_sevens += 1
    elif roll_total == 8:
        num_eights += 1
    elif roll_total == 9:
        num_nines += 1
    elif roll_total == 10:
        num_tens += 1
    elif roll_total == 11:
        num_elevens += 1
    elif roll_total == 12:
        num_twelves += 1
    else:
        print("Invalid roll — must be between 2 and 12")


    print(f'Roll {i} is {roll_total} ({die1} + {die2})')
    
print('\nDice roll statistics:')
print(f'2s: {"*" * num_twos}')
print(f'3s: {"*" * num_threes}')
print(f'4s: {"*" * num_fours}')
print(f'5s: {"*" * num_fives}')
print(f'6s: {"*"  *num_sixes}')
print(f'7s: {"*" * num_sevens}')
print(f'8s: {"*" * num_eights}')
print(f'9s: {"*" * num_nines}')
print(f'10s: {"*" * num_tens}')
print(f'11s: {"*" * num_elevens}')
print(f'12s: {"*" * num_twelves}')
