orders_record = {'Huy': 'cream', 'Ron': 'celery', 'Val': 'plum'}

my_input = ""

while my_input != "quit":
    my_input = input()
    
    if my_input in orders_record:
        del orders_record[my_input]
    elif my_input == "quit":
      break
    else:
        print(f"{my_input} not found")

print('Updated orders record:')
print(orders_record)