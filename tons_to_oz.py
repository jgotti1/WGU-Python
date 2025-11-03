#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
def oz_to_pounds(oz):
    tons = 0
    pounds = 0
    ounces = oz
    remainder = 0

    tons = (ounces // 16 ) // 2000
    remainder = (ounces / 16 ) % 2000
    pounds = remainder // 1
    remainder = remainder % 1
    ounces = 16 * remainder

    print(f"Tones: {tons}\nPounds: {pounds:.0f}\nOunces: {ounces:.0f}")




print("Enter the number of ounces to convert:")
ounces = int(input())
oz_to_pounds(ounces)
#convert ounces to pounds and tons 
#output number of tons, remaining pounds, and remaining ounces


#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

print("Enter the number of ounces to convert:")
ounces = int(input())

#convert ounces to pounds and tons 
ounces_left = ounces % 16 
tons = (ounces // 16) // 2000
pounds = (ounces // 16) - (2000 * tons)

#output number of tons, remaining pounds, and remaining ounces
print(ounces_left, pounds, tons)