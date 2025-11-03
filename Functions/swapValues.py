def swap_values(one, two, three, four):
    return two, one, four, three


user_val1 = int(input())
user_val2 = int(input())
user_val3 = int(input())
user_val4 = int(input())

a, b, c, d = swap_values(user_val1, user_val2, user_val3, user_val4)
print(a, b, c, d)