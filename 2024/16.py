# This implementation is done after studying the solution of Jonathan Paulson
# This is Dijkstra's algorithm
# For part 2 however, instead of breaking upon finding the shortest path
# let teh algorithm calculate the least distance for all nodes
# and then calculate from teh reverse direction as well
# length from start to node + length from node to end == shortest path
# this tells us whether a node is available on the optimal path or not
from heapq import heappush, heappop

with open("data") as file:
    content = file.readlines()

grid = []
line_count = 0
start = ""
end = ""
for line in content:
    row_data = [char for char in line.strip()]
    grid.append(row_data)
    if 'S' in row_data:
        start = (line_count, row_data.index('S'))
    if 'E' in row_data:
        end = (line_count, row_data.index('E'))
    line_count += 1

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
path = []
visited = set()
# start with the first node, which is at 0 distance with itself
# 0, r, c, direction (we are facing right)
heappush(path, (0, start[0], start[1], 1))
best_value = ""
forward_path = {}
while path:
    value, row, col, direction = heappop(path)
    # this dictionary stores value of the distance between the grid and the start point
    if (row, col, direction) not in forward_path.keys():
        forward_path[(row, col, direction)] = value
    if row == end[0] and col == end[1] and best_value == "":
        best_value = value
    if (row, col, direction) in visited:
        continue
    visited.add((row, col, direction))
    r, c = directions[direction]
    if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[0]):
        if grid[row+r][col+c] != '#':
            heappush(path, (value + 1, row + r, col + c, direction))
    heappush(path, (value + 1000, row, col, (direction + 1) % 4))
    heappush(path, (value + 1000, row, col, (direction + 3) % 4))

print("Part 1. The lowest score a Reindeer could possibly get = ", best_value)

path = []
visited = set()
backward_path = {}
# now we calculate the reverse path. Here we are free to start facing all directions.
for direction in range(4):
    heappush(path, (0, end[0], end[1], direction))
while path:
    value, row, col, direction = heappop(path)
    if (row, col, direction) not in backward_path.keys():
        backward_path[(row, col, direction)] = value
    if (row, col, direction) in visited:
        continue
    visited.add((row, col, direction))
    # why we need (direction+2) % 4
    # say we are in a grid facing up (index = 0)
    # when we go in reverse, we must move down (because we entered this grid up)
    # (0 + 2) % 4 = 2. and directions[2] points down
    r, c = directions[(direction+2) % 4]
    if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[0]):
        if grid[row+r][col+c] != '#':
            # but here we, keep the direction sane as that of the previous grid
            heappush(path, (value + 1, row + r, col + c, direction))
    heappush(path, (value + 1000, row, col, (direction + 1) % 4))
    heappush(path, (value + 1000, row, col, (direction + 3) % 4))

# now to find tiles which lie on the best paths
tiles_on_best_paths = set()
for row in range(len(grid)):
    for col in range(len(grid[0])):
        for direction in range(4):
            # if teh combination of row, col and direction exists on both forward and backward paths
            if (row, col, direction) in forward_path.keys() and (row, col, direction) in backward_path.keys():
                # and if their sum is the distance of the best path
                # the grid lies on the best path. hence, save the location
                if forward_path[(row, col, direction)] + backward_path[(row, col, direction)] == best_value:
                    tiles_on_best_paths.add((row, col))

print("Part 2. Tiles, that are part of at least one of the best paths through the maze = ", len(tiles_on_best_paths))
