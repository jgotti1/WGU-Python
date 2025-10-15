# Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

# i becomes 1
# a becomes @
# m becomes M
# B becomes 8
# s becomes $
# Ex: If the input is:

# mypassword
# the output is:

# Myp@$$word!


word = input()
password = ''

for character in word:
  if character == "i":
    password += "1"
  elif character == 'a':
    password += '@'
  elif character == 'm':
    password += 'M'
  elif character == 'B':
    password += '8'
  elif character == 's':
    password += '$'

  else:
    password += character
  
print(f"{password}!")
