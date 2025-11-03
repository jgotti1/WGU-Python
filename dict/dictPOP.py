food_data = {'plum': 'poor', 'carrot': 'fair', 'berry': 'good', 'cheese': 'great'}
price_chart = {'great': 50.0, 'good': 40.0, 'fair': 20.0, 'poor': 5.0}

food_name = input()

food_grade = food_data.pop(food_name, "N/A")

if food_grade != "N/A":
  patient_price = price_chart[food_grade]
else:
  patient_price = -99


print(f'{food_name} ({food_grade}) scores {patient_price}')
print('Remaining food:')
print(food_data)