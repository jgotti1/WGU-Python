# String string_data is read from input. If the first two characters are all lowercase, and the rest of the string is all uppercase, output "Valid". Otherwise, output "Invalid".

string_data = input()

if string_data[:2].islower() and string_data[2:].isupper():
  print("Valid")
else:
  print("Invalid")
  
