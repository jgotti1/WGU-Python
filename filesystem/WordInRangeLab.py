# Write a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. Your program should determine if the strings from the list are within that range (inclusive of the bounds) and output the results.

# Ex: If the input is:

# input1.txt
# ammoniated
# millennium
# and the contents of input1.txt are:

# aspiration
# classified
# federation
# graduation
# millennium
# philosophy
# quadratics
# transcript
# wilderness
# zoologists
# the output is:

# aspiration - in range
# classified - in range
# federation - in range
# graduation - in range
# millennium - in range
# philosophy - not in range
# quadratics - not in range
# transcript - not in range
# wilderness - not in range
# zoologists - not in range

# input_file = input()
input_file = 'input1.txt'
lower = input()
upper = input()


open_file = open(input_file, 'r')
lines = open_file.readlines()

for line in lines:
    line = line.strip()
    if lower <= line <= upper:
        print(f"{line} - in range")
    else:
        print(f"{line} - not in range")
    
open_file.close()

  
