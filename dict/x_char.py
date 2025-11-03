# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
  # Student code goes here
  return mystring[:x+1]
 
# expected output: WGU
print(printFirst('WGU College of IT', 3))   
 
# expected output: WGU College
print(printFirst('WGU College of IT', 11))