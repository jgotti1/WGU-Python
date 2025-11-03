# String data_entry is read from input with leading and trailing whitespaces. Remove any leading and trailing whitespaces in the string. If data_entry contains the string "Color:", capitalize the first letter for each word in data_entry. Otherwise, capitalize the first character in data_entry. Finally, print out the resulting string.

data_entry = input()

data_entry = data_entry.strip()

if "Color" in data_entry:
    data_entry = data_entry.title()
else:
  data_entry = data_entry.capitalize()
  
print(data_entry)
