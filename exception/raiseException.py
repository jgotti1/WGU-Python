try:
    tim_bought = int(input())  
    tim_sold = int(input())  
    if tim_bought < 1947:
        raise ValueError("Year of purchase cannot start before Tim's year of birth")
    if tim_sold  < tim_bought:
        raise ValueError('Year of sale cannot be before year of purchase')
    
    years_tim_owned = tim_sold - tim_bought

    print(f'Tim owned the house for {years_tim_owned} year(s)')

except ValueError as excpt:
    print(f'Error: {excpt}')