# Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase. The output should include the input character and use the plural form, n's, if the number of times the characters appears is not exactly 1.

# Ex: If the input is:

# n Monday
# the output is:

# 1 n
# Ex: If the input is:

# z Today is Monday
# the output is:

# 0 z's
# Ex: If the input is:

# n It's a sunny day
# the output is:

# 2 n's
# Case matters. n is different than N.

# Ex: If the input is:

# n Nobody
# the output is:

# 0 n's

my_input = input()

def char_count(my_input):
    input1, input2 = my_input.split(' ',1)
    count = 0
    i = 0
    for i in range(len(input2)):
        if input2[i] == input1:
            count = count +1
            i = i + 1
    if count == 1:
        print(f"{count} {input1}")
    else:
        print(f"{count} {input1}'s")

char_count(my_input)