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



# read from data file
with open("example") as file:
    content = file.readlines()

matrix = []
for line in content:
    matrix.append([char for char in line.strip()])

visited_positions = []
for row, entries in enumerate(matrix):
    for col, value in enumerate(entries):
        if (row, col) not in visited_positions:
            plot_positions = [(row, col)]
            find_plot(matrix[row][col], row, col)
            print(plot_positions)
