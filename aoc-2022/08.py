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

def find_scenic_value(row, col, value):
    row_values = grid[row]
    col_values = [grid[r][col] for r in range(len(grid))]
    # left
    left = 0
    for i in range(len(row_values[:col]), -1, -1):
        left += 1
        if row_values[i] >= value:
            break
    # right
    right = 0
    for i in range(col+1, len(grid[0])):
        right += 1
        if row_values[i] >= value:
            break
    # up
    up = 0
    for i in range(len(col_values[:row]), -1, -1):
        up += 1
        if col_values[i] >= value:
            break
    # down
    down = 0
    for i in range(row + 1, len(grid)):
        down += 1
        if col_values[i] >= value:
            break
    print(row, col, [up, left, down, right])
    return left * right * up  *down


with open("example") as file:
    content = file.readlines()

grid = []
for line in content:
    grid.append([int(value) for value in line.strip()])

visible_trees = 2 * len(grid[0]) + 2 * (len(grid) - 2)
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        if find_blocked_view(row, col, grid[row][col]) < 4:
            visible_trees += 1

        find_scenic_value(row, col, grid[row][col])
        #print(row, col, find_scenic_value(row, col, grid[row][col]))

print(visible_trees)