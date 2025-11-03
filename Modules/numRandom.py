import random

retries = 0  # Global required by assignment

def unique_random_ints(how_many, max_num):
    global retries
    retries = 0
    list_nums = []

    for num in range(how_many):
        num = random.randint(0, max_num)

        # Keep generating until unique
        while num in list_nums:
            retries += 1
            num = random.randint(0, max_num)

        list_nums.append(num)

    return f'{" ".join(str(n) for n in list_nums)} retries={retries}'


if __name__ == '__main__':
    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    random.seed(seed)
    print(unique_random_ints(how_many, max_num))
