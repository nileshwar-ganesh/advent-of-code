# This solution is quite similar to the one on Day 16
from heapq import heappush, heappop
import re

with open("d1") as file:
    content = file.readlines()

# grid dimensions
width = 71
height = 71
# creating a dot matrix of grid dimensions
grid = [['.' for _ in range(width)] for _ in range(height)]
# storing locations of all incoming byte locations
locations = []
for line in content:
    col, row = re.findall(r"\d+", line)
    locations.append((int(row), int(col)))

iteration = 0
while len(locations) > 0:
    is_path = False
    (row_byte, col_byte) = locations.pop(0)
    iteration += 1
    grid[row_byte][col_byte] = '#'
    # we are interested in grid after 1024th byte falls
    # so if iterations is less than that, simply continue
    if iteration < 1024:
        continue
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
    path = []
    start = (0, 0)
    end = (height - 1 , width - 1)
    visited = set()
    heappush(path, (0, 0, 0))
    while path:
        value, row, col = heappop(path)
        if row == end[0] and col == end[1]:
            # on 1024th iteration, publish the number of steps
            if iteration == 1024:
                print('Part 1. Minimum steps after 1024 bytes = {}'.format(value) )
            is_path = True
            break
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for direction in directions:
            (r, c) = direction
            if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[0]):
                if grid[row+r][col+c] != '#':
                    heappush(path, (value + 1, row + r, col + c))

    # if we fail to find a path, print the byte location and quit
    if not is_path:
        print('Part 2. Blocked path at position = {},{}'.format(col_byte, row_byte) )
        break