## App to total the miles traveled by three employees. requests input as to how many days they traveled and uses a fixed distance dictinary for the caluations

days_traveled = {
  "A" : int(input('how many days traveled employee A: ')),
  "B" : int(input('how many days traveled employee B: ')),
  "C" : int(input('how many days traveled employee C: ')),
}

miles_from_home = {
  "A": 13.62,
  "B": 15.87,
  "C": 22.01
}

total_miles = 0

for dict_key in days_traveled:
  print(f"{days_traveled[dict_key]} {miles_from_home[dict_key]}")
  total_miles = total_miles +  (miles_from_home[dict_key] * days_traveled[dict_key])

print(f"Your total miles between all three employees is: {total_miles:.2f}\n")
print('goodbye')
