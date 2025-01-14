from heapq import heappop, heappush
import sys

with open("data") as file:
    content = file.readlines()

grid = []
for line in content:
    grid.append([char for char in line.strip()])

def energize_beams(row, col, direction):
    beams = []
    directions = {".": {(0, 1): [(0, 1)], (1, 0): [(1, 0)], (0, -1): [(0, -1)], (-1, 0): [(-1, 0)]},
                  "/": {(0, 1): [(-1, 0)], (1, 0): [(0, -1)], (0, -1): [(1, 0)], (-1, 0): [(0, 1)]},
                  "\\": {(0, 1): [(1, 0)], (1, 0): [(0, 1)], (0, -1): [(-1, 0)], (-1, 0): [(0, -1)]},
                  "|": {(0, 1): [(-1, 0), (1, 0)], (1, 0): [(1, 0)], (0, -1): [(1, 0), (-1, 0)], (-1, 0): [(-1, 0)]},
                  "-": {(0, 1): [(0, 1)], (1, 0): [(0, -1), (0, 1)], (0, -1): [(0, -1)], (-1, 0): [(0, -1), (0, 1)]}
                  }
    heappush(beams, (row, col, direction))
    visited_tile = []
    seen = set()
    count = 0
    while beams:
        row, col, direction = heappop(beams)
        if (row, col) not in seen:
            seen.add((row, col))
        if (row, col, direction) in visited_tile:
            continue
        visited_tile.append((row, col, direction))
        tile = grid[row][col]
        for dir in directions[tile][direction]:
            r = row + dir[0]
            c = col + dir[1]
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if (r, c, dir) not in visited_tile:
                    heappush(beams, (r, c, dir))
    return len(seen)

max_value = 0
for col, char in enumerate(grid[0]):
    value = energize_beams(0, col, (1, 0))
    if value > max_value:
        max_value = value
print("Completed first row")
for col, char in enumerate(grid[-1]):
    value = energize_beams(len(grid)-1, col, (-1, 0))
    if value > max_value:
        max_value = value
print("Completed last row")
for row, char in enumerate(grid):
    value = energize_beams(row, 0, (0, 1))
    if value > max_value:
        max_value = value
print("Completed first col")
for row, char in enumerate(grid):
    value = energize_beams(row, len(grid[0]) - 1, (0, -1))
    if value > max_value:
        max_value = value
print("Completed last col")
print(max_value)
