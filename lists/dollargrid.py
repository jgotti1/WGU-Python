grid_size = int(input())

pattern_grid = []
for p in range(grid_size):
    row = []
    for q in range(grid_size):
        row.append('.')
    pattern_grid.append(row)

for p in range(grid_size):
    for q in range(grid_size):
        if (p + q) >= (grid_size - 1):
            pattern_grid[p][q] = '$'

for row in pattern_grid:
    for cell in row:
        print(cell, end='')
    print()
