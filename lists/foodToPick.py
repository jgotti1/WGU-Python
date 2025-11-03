# List food_to_pick contains words read from the first line of input. List allergies_list contains words read from the second line of input. For each element in food_to_pick that is also in allergies_list:

# Output the element, followed by ' not an option'.
# Remove the element from food_to_pick.
# Click here for example
# Ex: If the input is:

# tea pear butter beans
# milk beans tea
# then the output is:

# Food on menu: tea pear butter beans 
# Food allergies: milk beans tea 
# tea not an option
# beans not an option
# Safe food: pear butter

food_to_pick = input().split()
allergies_list = input().split()
  
print('Food on menu:', end=' ')
for food in food_to_pick:
    print(food, end=' ')
print()

print('Food allergies:', end=' ')
for food in allergies_list:
    print(food, end=' ')
print()

for value in food_to_pick[:]:
  if value in allergies_list:
    print(f'{value} not an option')
    food_to_pick.remove(value)

print('Safe food:', end=' ')
for food in food_to_pick:
    print(food, end=' ')
print()