
# Define a function find_price_per_menu() that takes one parameter as the number of people attending a dinner, and returns the menu's price. The menu's price is returned as follows:

# If the number of people is at least 550, then the menu price is $47.
# If the number of people is more than 175 and less than 550, then the menu price is $56.
# Otherwise, the menu price is $70.

def find_price_per_menu(np):
  if np >= 550:
    return 47
  elif np > 175 and np < 550:
    return 56
  else:
    return 70
  

input_guest_number = int(input())

print(f'Testing 178: {find_price_per_menu(178)}')
print(f'Testing user input: {find_price_per_menu(input_guest_number)}')