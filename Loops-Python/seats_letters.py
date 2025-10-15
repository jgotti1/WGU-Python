# example output
# A1 A2 A3 A4
# B1 B2 B3 B4


num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))

# for r in range(num_rows):
#   current_row_letter = "A"
#   for c in range(num_columns):
#     print(f'{current_row_letter}{r + 1 }', end=' ')
#     current_row_letter = chr(ord(current_row_letter) + 1)
#   print()  
  
  
current_row_letter = "A"
for r in range(num_rows):
  for c in range(num_columns):
    print(f'{current_row_letter}{c + 1 }', end=' ')
  current_row_letter = chr(ord(current_row_letter) + 1)
  print()  