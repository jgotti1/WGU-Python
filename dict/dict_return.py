# Complete the function to return a dictionary using 
# list1 as the keys and list2 as the values
def createDict(list1, list2):

  mydict = {}
  
  for i in range(len(list1)):
    mydict[list1[i]] = list2[i]
  return mydict
    
    
        
# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}  
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))        
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))