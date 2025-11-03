# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
  
  if mystring.startswith("WGU"):
    return mystring
  elif "WGU" in mystring:
    return mystring.replace("WGU", "")
  else:
    return
 
  

    
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))