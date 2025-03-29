import re


with open("example") as file:
    content = file.readlines()

# creating a readable matrix out of input d1
directions = []
grid = []
is_direction = False
line_count = 0
start = ""

for line in content:
    if line == "\n":
        is_direction = True
        continue
    else:
        if not is_direction:
            row_data = [char for char in line.strip()]
            grid.append(row_data)
            if '@' in row_data:
                start = (line_count, row_data.index('@'))
        else:
            for char in line.strip():
                directions.append(char)
    line_count += 1


#print(directions)
#for line in grid:
#    print(line)
D = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
row = start[0]
col = start[1]
# directions = ['v', '^', '^', '>']
for d in directions:
    r = row + D[d][0]
    c = col + D[d][1]
    if grid[r][c] == '.':
        grid[row][col] = '.'
        grid[r][c] = '@'
        row, col = r, c
    elif grid[r][c] == '#':
        continue
    elif grid[r][c] == 'O':
        mr = r
        mc = c
        wall = False
        while grid[mr][mc] != '.':
            mr += D[d][0]
            mc += D[d][1]
            if grid[mr][mc] == '#':
                wall = True
                break
        if not wall and (mr != r or mc != c):
            while True:
                grid[mr][mc] = 'O'
                mr -= D[d][0]
                mc -= D[d][1]
                if mr == r and mc == c:
                    grid[r][c] = '@'
                    grid[row][col] = '.'
                    row, col = r, c
                    break

total = 0
for row, line in enumerate(grid):
    print(line)
    for col, value in enumerate(line):
        if value == 'O':
            total += 100*row + col

print(total)
