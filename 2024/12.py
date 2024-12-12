def find_plot(value, row, col):
    global plot_positions, visited_positions
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1) ]
    for d in direction:
        r = row + d[0]
        c = col + d[1]
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            if matrix[r][c] == value and (r, c) not in plot_positions:
                plot_positions.append((r, c))
                find_plot(value, r, c)
                if (r, c) not in visited_positions:
                    visited_positions.append((r, c))

def find_perimeter(plot):
    global plot_positions
    perimeter = 0
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1) ]
    for d in direction:
        r = plot[0] + d[0]
        c = plot[1] + d[1]
        if (r, c) not in plot_positions:
            perimeter += 1
    return perimeter


# read from data file
with open("data") as file:
    content = file.readlines()

matrix = []
for line in content:
    matrix.append([char for char in line.strip()])

visited_positions = []
fencing = 0
for row, entries in enumerate(matrix):
    for col, value in enumerate(entries):
        if (row, col) not in visited_positions:
            plot_positions = [(row, col)]
            find_plot(matrix[row][col], row, col)
            area = len(plot_positions)
            perimeter = 0
            for plot in sorted(plot_positions):
                perimeter += find_perimeter(plot)
            fencing += area * perimeter
            print(matrix[row][col], area, perimeter, fencing)

print(fencing)
