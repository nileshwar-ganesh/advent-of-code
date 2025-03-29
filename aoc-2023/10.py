from heapq import heappush, heappop

def find_start_tile():
    opening = {"top": 0, "right": 0, "bot": 0, "left": 0}
    # direction text (top, right, ...) and direction value ((-1, 0), (0, 1), ...)
    for dt, dv in direction.items():
        r = start[0] + dv[0]
        c = start[1] + dv[1]
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            pair_direction = dt
            if grid[r][c] in connectors[connection_pair[pair_direction]]:
                opening[connection_pair[pair_direction]] = 1

    tile_opening = [key for key in opening.keys() if opening[key] == 1]
    for key, value in out_map.items():
        if sorted(value) == sorted(tile_opening):
            return key


with open("d1") as file:
    content = file.readlines()

grid = []
start = None
for row, line in enumerate(content):
    entries = [char for char in line.strip()]
    if 'S' in entries:
        col = entries.index('S')
        start = (row, col)
    grid.append(entries)

out_map = {"F": ["right", "bot"], "7": ["left", "bot"], "J": ["left", "top"],
           "L": ["right", "top"], "-": ["left", "right"], "|": ["top", "bot"],
           ".": []}
direction = {"top": (-1, 0), "right": (0, 1), "bot": (1, 0), "left": (0, -1)}
connection_pair = {"left": "right", "right": "left", "top": "bot", "bot": "top"}
connectors = {"left": ["-", "J", "7"], "right": ["-", "F", "L"],
              "top": ["|", "J", "L"], "bot": ["|", "F", "7"]}

# find start tile with 'S' and replace with one of the correct values (F, -, 7, |, J, L)
grid[start[0]][start[1]] = find_start_tile()
# map which maintains the correct distance
tiles_distance = {start: 0}
# marker for all visited tiles
visited_tiles = set()
# the actual loop
path = []
heappush(path, (0, start[0], start[1]))
while path:
    distance, row, col = heappop(path)
    # add this to visited tiles
    if (row, col) not in tiles_distance.keys():
        tiles_distance[(row, col)] = distance
    if (row, col) in visited_tiles:
        continue
    visited_tiles.add((row, col))
    for d in out_map[grid[row][col]]:
        r = row + direction[d][0]
        c = col + direction[d][1]
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            # only if the adjacent tile is the correct connector
            # else, ignore
            if grid[r][c] in connectors[connection_pair[d]]:
                heappush(path, (distance + 1, r, c))

print('Part 1. Farthest point from starting position = ', max(tiles_distance.values()))







