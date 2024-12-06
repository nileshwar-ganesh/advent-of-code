import copy

with open("data") as file:
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
for r, _ in enumerate(path_matrix):
    print("Current row = ", r)
    for c, val in enumerate(path_matrix[0]):
        r = 17
        c = 7
        path_matrix_cp = copy.deepcopy(path_matrix)
        if val != '#':
            path_matrix_cp[r][c] = '#'
            for i in range(4):
                position_cp = []
                direction_cp = []
                if i == 0:
                    # top left check
                    if 0 <= r+1 < len(path_matrix):
                        if path_matrix_cp[r+1][c] == '#':
                            continue
                    position_cp.append((r + 1, c))
                    direction_cp.append((0, 1))
                elif i == 1:
                    # top right check
                    if 0 <= c - 1 < len(path_matrix[0]):
                        if path_matrix_cp[r][c - 1] == '#':
                            continue
                    position_cp.append((r, c - 1))
                    direction_cp.append((1, 0))
                elif i == 2:
                    # bot right check
                    if 0 <= r - 1 < len(path_matrix):
                        if path_matrix_cp[r - 1][c] == '#':
                            continue
                    position_cp.append((r - 1, c))
                    direction_cp.append((0, -1))
                elif i == 3:
                    # bot left check
                    if 0 <= c + 1 < len(path_matrix[0]):
                        if path_matrix_cp[r][c + 1] == '#':
                            continue
                    position_cp.append((r, c + 1))
                    direction_cp.append((-1, 0))

                print(position_cp, direction_cp)

                while True:
                    row = position_cp[-1][0] + direction_cp[-1][0]
                    col = position_cp[-1][1] + direction_cp[-1][1]
                    if 0 <= row < len(path_matrix_cp) and 0 <= col < len(path_matrix_cp[0]):
                        if path_matrix_cp[row][col] == '#':
                            print("here")
                            if direction_cp[-1] == (0, -1):
                                direction_cp.append((-1, 0))
                            elif direction_cp[-1] == (-1, 0):
                                direction_cp.append((0, 1))
                            elif direction_cp[-1] == (0, 1):
                                direction_cp.append((1, 0))
                            elif direction_cp[-1] == (1, 0):
                                direction_cp.append((0, -1))
                        else:
                            print(row, col)
                            if direction_cp[-1] == (-1, 0) and col != c:
                                break
                            if position_cp.count((row, col)) > 4:
                                loop_positions.append((r, c))
                                break
                            position_cp.append((row, col))
                            if row <= 0 or row >= len(path_matrix_cp) - 1 or col <= 0 or col >= len(path_matrix_cp[0]) - 1:
#                                print("valid exit")
                                break
                    else:
                        break
#                print("it did break")
#        break
#    break
print(len(set(loop_positions)))