# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
      count = 0
      for i in range(len(mystring)):
        if mystring[i].isupper():
          count += 1
      return count
        
def countUpper2(mystring):    
      count = 0
      i = 0
      while i < len(mystring):
        if mystring[i].isupper():
          count = count + 1 
        i = i + 1
      return count
    
    
          
        

      
      
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))

# expected output: 4
print(countUpper2('Welcome to WGU'))
 
# expected output: 2
print(countUpper2('Hello, Mary'))