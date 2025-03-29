import numpy as np

def calculate_load(grid):
    total = 0
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            value = len(grid) - i
            if grid[i, j] == "O":
                total += value
    return total

def tilt_platform_cycle(grid, is_part_2=False):
    # up
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i, j] == "O" or grid[i, j] == "#":
                continue
            ir = i + 1
            if 0 <= ir < len(grid):
                while grid[ir, j] == ".":
                    ir += 1
                    if ir == len(grid):
                        break
                if 0 <= ir < len(grid):
                    if grid[ir, j] == "O":
                        grid[ir, j] = "."
                        grid[i, j] = "O"

    if not is_part_2:
        return grid

    # left
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i, j] == "O" or grid[i, j] == "#":
                continue
            jc = j + 1
            if 0 <= jc < len(grid[0]):
                while grid[i, jc] == ".":
                    jc += 1
                    if jc == len(grid[0]):
                        break
                if 0 <= jc < len(grid[0]):
                    if grid[i, jc] == "O":
                        grid[i, jc] = "."
                        grid[i, j] = "O"
    # down
    for j in range(len(grid[0])):
        for ia in range(len(grid)):
            i = len(grid) - ia - 1
            if grid[i, j] == "O" or grid[i, j] == "#":
                continue
            ir = i - 1
            if 0 <= ir < len(grid):
                while grid[ir, j] == ".":
                    ir -= 1
                    if ir < 0:
                        break
                if 0 <= ir < len(grid):
                    if grid[ir, j] == "O":
                        grid[ir, j] = "."
                        grid[i, j] = "O"
    # right
    for i in range(len(grid)):
        for ja in range(len(grid[0])):
            j = len(grid[0]) - ja - 1
            if grid[i, j] == "O" or grid[i, j] == "#":
                continue
            jc = j - 1
            if 0 <= jc < len(grid[0]):
                while grid[i, jc] == ".":
                    jc -= 1
                    if jc < 0:
                        break
                if 0 <= jc < len(grid[0]):
                    if grid[i, jc] == "O":
                        grid[i, jc] = "."
                        grid[i, j] = "O"
    return grid

with open("d1") as file:
    content = file.readlines()

grid = []
for line in content:
    grid.append([char for char in line.strip()])
grid = np.array(grid)

tilt_platform_cycle(grid)
total_load_1 = calculate_load(grid)

matrix = []
found = False
index = None
steps = 1000000000
for i in range(steps):
    grid_list = grid.tolist()
    for entry in matrix:
        if entry == grid_list :
            step = i - matrix.index(grid_list)
            index = matrix.index(grid_list) + ((steps - matrix.index(grid_list)) % step)
            found = True
    if found:
        break
    matrix.append(grid_list)
    grid = tilt_platform_cycle(grid, True)

total_load_2 = calculate_load(np.array(matrix[index]))

print("Part 1. Total load on north support beams after one tilt = ", total_load_1)
print("Part 2. Total load on north support beams after 1000000000 cycles = ", total_load_2)



