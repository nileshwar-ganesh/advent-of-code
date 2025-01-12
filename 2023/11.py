
def calculate_distance(is_part_2=False):
    if is_part_2:
        duplicate = 999999
    else:
        duplicate = 1
    total_distance = 0
    for idx, source in enumerate(galaxy_pos):
        for destination in galaxy_pos[idx + 1: ]:
            row_start = min(source[0], destination[0])
            row_end = max(source[0], destination[0]) + 1
            col_start = min(source[1], destination[1])
            col_end = max(source[1], destination[1]) + 1
            rows = [value for value in range(row_start, row_end)]
            cols = [value for value in range(col_start, col_end)]
            overlap = len(set(rows) & set(empty_rows)) + len(set(cols) & set(empty_cols))
            distance = len(rows) - 1 + len(cols) - 1 + (overlap * duplicate)
            total_distance += distance
    return total_distance

with open("data") as file:
    content = file.readlines()

grid = []
row = 0
empty_rows = []
empty_cols = [col for col, char in enumerate(content[0].strip())]
galaxy_pos = []
for col, line in enumerate(content):
    line = [char for char in line.strip()]
    grid.append(line)
    if '#' not in line:
        empty_rows.append(row)
    non_empty_pos = [pos for pos, char in enumerate(line) if char == '#']
    for pos in non_empty_pos:
        galaxy_pos.append((row, pos))
        if pos in empty_cols:
            empty_cols.pop(empty_cols.index(pos))
    row += 1

print('Part 1. Sum of distances between galaxies = ', calculate_distance())
print('Part 2. Sum of distances between expanded galaxies = ', calculate_distance(True))
