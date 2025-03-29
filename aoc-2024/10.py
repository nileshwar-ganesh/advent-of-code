# recursive function which calculates trail to the peak
def find_peak(value, row, col):
    # using a global variable counter to hold the positions of peak (value = 9)
    global counter
    # the direction is either one step left or right / top or bottom
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    # if we reach a peak, we need to store that (row, col)
    if value == 9:
        counter.append((row, col))
        return True
    # else, look for the next higher number in the boundary cell
    for d in direction:
        r = row + d[0]
        c = col + d[1]
        if 0 <= row + d[0] < len(matrix) and 0 <= col + d[1] < len(matrix[0]):
            # if the value matches, recursively call the function
            if matrix[row + d[0]][col + d[1]] == value + 1:
                find_peak(value + 1, r, c)

# read from d1 file
with open("d1") as file:
    content = file.readlines()

# creating a readable matrix out of input d1
matrix = []
for line in content:
    matrix.append([int(char) for char in line.strip()])

total_unique_trailheads = 0
total_unique_paths = 0
for row, entry in enumerate(matrix):
    for col, val in enumerate(matrix[0]):
        counter = []
        if matrix[row][col] == 0:
            find_peak( 0, row, col)
            total_unique_trailheads += len(set(counter))
            total_unique_paths += len(counter)
print("Part 1. Total unique trailheads from every 0 position = ", total_unique_trailheads)
print("Part 2. Total unique paths to trailheads from every 0 position = ", total_unique_paths)


