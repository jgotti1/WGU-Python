# 10.7 LAB: Fat-burning heart rate
# lab activity
# 10.7.1: LAB: Fat-burning heart rate

# Full screen
# 0 / 10
# Write a program that calculates an adult's fat-burning heart rate, which is 70% of the difference between 220 and the person's age respectively. Complete fat_burning_heart_rate() to calculate the fat burning heart rate.

# The adult's age must be between the ages of 18 and 75 inclusive. If the age entered is not in this range, raise a ValueError exception in get_age() with the message "Invalid age." Handle the exception in __main__ and print the ValueError message along with "Could not calculate heart rate info."

# Ex: If the input is:

# 35
# the output is:

# Fat burning heart rate for a 35 year-old: 129.5 bpm
# If the input is:

# 17
# the output is:

# Invalid age.
# Could not calculate heart rate info.

def get_age():
    age = int(input())
    # TODO: Raise exception for invalid ages
    if age < 18 or age >= 75:
      raise ValueError("Invaild age")
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .70
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
  try:
    age = get_age()
    heart_rate = fat_burning_heart_rate(age)
    print(f'Fat burning heart rate for a {age} year-old: {heart_rate} bpm')
 
  except ValueError as exc:
   print(exc)
   print("Could not calculate heart rate info.")