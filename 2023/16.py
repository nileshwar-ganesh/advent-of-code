from heapq import heappop, heappush

with open("data") as file:
    content = file.readlines()

grid = []
for line in content:
    grid.append([char for char in line.strip()])

beams = []
directions = {".": {(0, 1): [(0, 1)], (1, 0): [(1, 0)], (0, -1): [(0, -1)], (-1, 0): [(-1, 0)]},
              "/": {(0, 1): [(-1, 0)], (1, 0): [(0, -1)], (0, -1): [(1, 0)], (-1, 0): [(0, 1)]},
              "\\": {(0, 1): [(1, 0)], (1, 0): [(0, 1)], (0, -1): [(-1, 0)], (-1, 0): [(0, -1)]},
              "|": {(0, 1): [(-1, 0), (1, 0)], (1, 0): [(1, 0)], (0, -1): [(1, 0), (-1, 0)], (-1, 0): [(-1, 0)]},
              "-": {(0, 1): [(0, 1)], (1, 0): [(0, -1), (0, 1)], (0, -1): [(0, -1)], (-1, 0): [(0, -1), (0, 1)]}
              }
heappush(beams, (0, 0, (0, 1)))
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

print(len(seen))