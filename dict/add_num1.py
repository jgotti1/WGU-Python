# Complete the function to add num1 to the end of the given list
def addToEnd(mylist, num1):
# Student code goes here
  mylist.append(num1)
  return mylist
 
# expected output: [4, 5, 6, 7]
print(addToEnd([4,5,6], 7))
 
# expected output: [9, 8, 7, 6]
print(addToEnd([9,8,7], 6))