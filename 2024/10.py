def find_peak(value, position):
    for pos in position:
        row = pos[0]
        col = pos[1]
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        found = []
        for d in direction:
            if 0 <= row + d[0] < len(matrix) and 0 <= col + d[1] < len(matrix[0]):
                if matrix[row + d[0]][col + d[1]] == value + 1:
                    r = row + d[0]
                    c = col + d[1]
                    found.append((r, c))
        if len(found) >= 1 and value < 9:
            for entry in found:
                find_peak(value + 1, entry)
        else:
            return False


with open("example") as file:
    content = file.readlines()

# creating a readable matrix out of input data
matrix = []
for line in content:
    matrix.append([int(char) for char in line.strip()])

valley_positions = []
for row, entry in enumerate(matrix):
    for col, value in enumerate(matrix[0]):
        if matrix[row][col] == 0:
            valley_positions.append((row, col))

for position in valley_positions:
    print(find_peak(0, [position]))

print(valley_positions)

