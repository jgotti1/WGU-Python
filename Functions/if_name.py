def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon ) * dollars_per_gallon
# used for zbooks grading the if_name
if __name__ == '__main__':
    miles_per_gallon = float(input())   
    dollars_per_gallon = float(input())

    total_cost_10m = driving_cost(miles_per_gallon, dollars_per_gallon, 10)
    total_cost_50m = driving_cost(miles_per_gallon, dollars_per_gallon, 50)
    total_cost_400m = driving_cost(miles_per_gallon, dollars_per_gallon, 400)

    print(f'{total_cost_10m:.2f}')
    print(f'{total_cost_50m:.2f}')
    print(f'{total_cost_400m:.2f}')