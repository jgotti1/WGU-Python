# Complete the function to remove the third item in the given list
def removeThird(mylist):
# Student code goes here
  mylist.remove(mylist[2])
  return mylist
 
# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))
 
# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))