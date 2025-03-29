import copy
import sys

with open("d1") as file:
    content = file.readlines()

path_matrix = []
position = []
direction = []
line_num = 0
occupied_cells = []
for line in content:
    values = [i for i in line.strip()]
    path_matrix.append(values)
    if "<" in values:
        position.append((line_num, values.index("<")))
        direction.append((0, -1))
    elif ">" in values:
        position.append((line_num, values.index(">")))
        direction.append((0, 1))
    elif "^" in values:
        position.append((line_num, values.index("^")))
        direction.append((-1, 0))
    elif "v" in values:
        position.append((line_num, values.index("v")))
        direction.append((1, 0))

    for c, val in enumerate(values):
        if val == '#' or val == '^' :
            occupied_cells.append((line_num, c))
    line_num += 1

path_matrix_cp = copy.deepcopy(path_matrix)
position_cp = copy.deepcopy(position)
direction_cp = copy.deepcopy(direction)
while True:
    row = position_cp[-1][0] + direction_cp[-1][0]
    col = position_cp[-1][1] + direction_cp[-1][1]
    if 0 <= row < len(path_matrix_cp) and 0 <= col < len(path_matrix_cp[0]):
        if path_matrix_cp[row][col] == '#':
            if direction_cp[-1] == (0, -1):
                direction_cp.append((-1, 0))
            elif direction_cp[-1] == (-1, 0):
                direction_cp.append((0, 1))
            elif direction_cp[-1] == (0, 1):
                direction_cp.append((1, 0))
            elif direction_cp[-1] == (1, 0):
                direction_cp.append((0, -1))
        else:
            position_cp.append((row, col))
            if row == 0 or row == len(path_matrix_cp) - 1 or col == 0 or col == len(path_matrix_cp[0]) - 1:
                break

print(len(set(position_cp)))
loop_positions = []
positions = set(position_cp)
path_matrix_cp = copy.deepcopy(path_matrix)
position_cp = copy.deepcopy(position)
direction_cp = copy.deepcopy(direction)

for idx, pos in enumerate(positions):
    if idx % 100 == 0:
        print(idx)
    path_matrix_cp = copy.deepcopy(path_matrix)
    position_cp = copy.deepcopy(position)
    direction_cp = copy.deepcopy(direction)
    path_matrix_cp[pos[0]][pos[1]] = '#'
    while True:
        row = position_cp[-1][0] + direction_cp[-1][0]
        col = position_cp[-1][1] + direction_cp[-1][1]
        if 0 <= row < len(path_matrix_cp) and 0 <= col < len(path_matrix_cp[0]):
            if path_matrix_cp[row][col] == '#':
                if direction_cp[-1] == (0, -1):
                    direction_cp.append((-1, 0))
                elif direction_cp[-1] == (-1, 0):
                    direction_cp.append((0, 1))
                elif direction_cp[-1] == (0, 1):
                    direction_cp.append((1, 0))
                elif direction_cp[-1] == (1, 0):
                    direction_cp.append((0, -1))
            else:
                if position_cp.count((row, col)) > 4:
                    loop_positions.append(pos)
                    break
                position_cp.append((row, col))
                if row == 0 or row == len(path_matrix_cp) - 1 or col == 0 or col == len(path_matrix_cp[0]) - 1:
                    break

print(len(loop_positions))