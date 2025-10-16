# A quick pick python program to seletc your lottery numbers

import random

selection = 0
exit = False

while not exit:
    print("Select the type of quick pick")
    print("1. Quick Pick Three")
    print("2. Quick Pick Four")
    print("3. Quick Pick Six")
    selection = int(input("Select Option 1, 2, or 3: "))
    print()
    
    if selection == 1:
        selection = 3
        exit = True
    elif selection == 2:
        selection = 4
        exit = True
    elif selection == 3:
        selection = 6
        exit = True
    else:
        print("Dummy, thats not a choice, try again")
        print()
       
if selection == 6:
  top = 99
else:
  top = 9
  
how_many = int(input("How many quick picks do you want? "))
print()

# get a random # between 1 - 99 (top) and get x amount of numbers (selection)
print("Here are your numbers. Good Luck !")
print()

for _ in range(how_many):
    picks = random.sample(range(1, top), selection)  
    print(*picks, sep=' ')
   
print()
print("Goodbye... play again soon")