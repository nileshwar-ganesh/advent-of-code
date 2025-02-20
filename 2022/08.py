def find_blocked_view(row, col, value):
    row_values = grid[row]
    col_values = [grid[r][col] for r in range(len(grid))]
    blocked = 0
    # left
    if max(row_values[:col]) >= value:
        blocked += 1
    # right
    if max(row_values[col+1:]) >= value:
        blocked += 1
    # up
    if max(col_values[:row]) >= value:
        blocked += 1
    # down
    if max(col_values[row+1:]) >= value:
        blocked += 1

    return blocked

with open("data") as file:
    content = file.readlines()

grid = []
for line in content:
    grid.append([int(value) for value in line.strip()])

visible_trees = 2 * len(grid[0]) + 2 * (len(grid) - 2)
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        if find_blocked_view(row, col, grid[row][col]) < 4:
            visible_trees += 1

print(visible_trees)