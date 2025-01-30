from heapq import heappop, heappush
import numpy as np
with open("data") as file:
    content = file.readlines()

grid = []
for line in content:
    grid.append([int(char) for char in line.strip()])

path = []
cost_map = {}
start = (0, 0)
end = (len(grid) - 1, len(grid[0]) - 1)
heappush(path, (0, 0, 0, (0, 1), 0))
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
visited_tiles = []
while path:
    cost, row, col, direction, steps = heappop(path)
    if (row, col) == end:
        print(cost)
        break
    for index, d in enumerate(directions):
        if index == (directions.index(direction) + 2) % 4:
            continue
        if steps == 3 and d == direction:
            continue
        r = row + d[0]
        c = col + d[1]
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if d == direction:
                step = steps + 1
            else:
                step = 1
            if step > 3:
                continue
            new_cost = cost + grid[r][c]
            if (r, c, d, step) in visited_tiles:
                continue
            visited_tiles.append((r, c, d, step))
            heappush(path, (new_cost, r, c, d, step))

