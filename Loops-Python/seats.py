#  Integers num_rows and num_columns are read from input representing the number of rows and columns of a theater's seating plan. Complete the nested for loop to output each seat label, as shown in the example. Each seat label is followed by a space, and each row is followed by a newline.

# Step 1
# Define the outer for loop with no indentation to iterate through each row of the theater. Use the loop variable current_row and iterate num_rows times, starting with integer 1.

# Step 2
# In the outer loop's body, use one indentation to add a statement to initialize current_column_letter with 'A'.

# Step 3
# In the outer loop's body, define the inner for loop to iterate through each column of the theater. Use the loop variable current_column and iterate num_columns times, starting with integer 1.

# Ex: If the input is:
# 2
# 3
# then the output is:
# 1A 1B 1C 
# 2A 2B 2C 
# Note: Statements with one indentation are in the outer loop's body.

num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))

for r in range(num_rows):
    current_column_letter = "A"
    for c in range(num_columns):
        # Inner for loop statements
        current_row = r + 1
        print(f'{current_row}{current_column_letter}', end=' ')
        current_column_letter = chr(ord(current_column_letter) + 1)  # Used to increment letters
    print()
