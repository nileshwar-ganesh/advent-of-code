# This solution is quite similar to the one on Day 16
import copy, sys
from heapq import heappush, heappop
import re

with open("example") as file:
    content = file.readlines()

# storing locations of all incoming byte locations
grid = []
row = 0
start = None
end = None
for line in content:
    row_content = []
    for col, char in enumerate(line.strip()):
        row_content.append(char)
        if char == 'S':
            start = (row, col)
        if char == 'E':
            end = (row, col)
    grid.append(row_content)
    row += 1


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
path = []
original_path = set()
heappush(path, (0, start[0], start[1]))
shortest_path_length = None
distance_map = {}
while path:
    value, row, col = heappop(path)
    if row == end[0] and col == end[1]:
        shortest_path_length = value
        break
    if (row, col) in original_path:
        continue
    original_path.add((row, col))
    distance_map[(row, col)] = value
    for direction in directions:
        (r, c) = direction
        if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[0]):
            if grid[row+r][col+c] != '#':
                heappush(path, (value + 1, row + r, col + c))

cheat_length = 2
for key, value in distance_map.items():
    row, col = key
    for cheat in range(cheat_length):
        continue


