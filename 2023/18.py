import copy
import re
from heapq import heappush, heappop

with open("data") as file:
    content = file.readlines()

pattern = r'#[0-9a-fA-F]{6}'
directions = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
instructions = []
for line in content:
    direction, steps, color = line.strip().split(" ")
    instructions.append([direction, int(steps), re.findall(pattern, color)[0]])

tile = (0, 0)
positions = []
for instruction in instructions:
    direction, steps, color = instruction[0], instruction[1], instruction[2]
    for _ in range(0, steps):
        heappush(positions, tile)
        tile = (tile[0]+directions[direction][0], tile[1]+directions[direction][1])

grid = []
line = []
while positions:
    row, col = heappop(positions)
    if not line:
        line.append((row, col))
        continue
    if row != line[-1][0]:
        grid.append(copy.deepcopy(line))
        line = []
        line.append((row, col))
        continue
    line.append((row, col))
if line:
    grid.append(line)

#grid = [[(0, 0), (0, 1), (0, 5), (0, 8), (0, 11)]]
for line in grid:
    print(line)
tile_count = 0
for line in grid:
    previous_entry = ""
    is_included = False
    line_count = 0
    for entry in line:
        row, col = entry[0], entry[1]
        if not str(previous_entry).isnumeric():
            previous_entry = col
            line_count += 1
            continue
        if col != previous_entry + 1:
            is_included = not is_included
            if is_included:
                line_count += col - previous_entry
            else:
                line_count += 1
        else:
            line_count += 1
        previous_entry = col
    tile_count += line_count
print(tile_count)


