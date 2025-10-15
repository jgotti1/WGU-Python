input_count = int(input())

examinees_list = []
for i in range(input_count):
    examinees_list.append(input())
    
for person in examinees_list:
  if (examinees_list.index(person)) % 2 == 0:
    print(f"{person} goes to level 2")
  else:
    print(f"{person} goes to level 1")
    

  