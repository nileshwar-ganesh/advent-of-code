# function to find the XMAS (Part 1)
def xmas_word_map(r, c, matrix):
    count = 0
    if 0 <= r - 3 < len(matrix):
        if 0 <= c - 3 < len(matrix):
            word = matrix[r][c] + matrix[r-1][c-1] + matrix[r-2][c-2] + matrix[r-3][c-3]
            if word == 'XMAS':
                count += 1
        word = matrix[r][c] + matrix[r-1][c] + matrix[r-2][c] + matrix[r-3][c]
        if word == 'XMAS':
            count += 1
        if 0 <= c + 3 < len(matrix):
            word = matrix[r][c] + matrix[r-1][c+1] + matrix[r-2][c+2] + matrix[r-3][c+3]
            if word == 'XMAS':
                count += 1
    if 0 <= r + 3 < len(matrix):
        if 0 <= c - 3 < len(matrix):
            word = matrix[r][c] + matrix[r+1][c-1] + matrix[r+2][c-2] + matrix[r+3][c-3]
            if word == 'XMAS':
                count += 1
        word = matrix[r][c] + matrix[r+1][c] + matrix[r+2][c] + matrix[r+3][c]
        if word == 'XMAS':
            count += 1
        if 0 <= c + 3 < len(matrix):
            word =  matrix[r][c] + matrix[r+1][c+1] + matrix[r+2][c+2] + matrix[r+3][c+3]
            if word == 'XMAS':
                count += 1
    if 0 <= c - 3 < len(matrix[0]):
        word = matrix[r][c] + matrix[r][c-1] + matrix[r][c-2] + matrix[r][c-3]
        if word == 'XMAS':
            count += 1
    if 0 <= c + 3 < len(matrix[0]):
        word = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r][c+3]
        if word == 'XMAS':
            count += 1
    return count

# function to find the MAS in form of X (Part 2)
def mas_word_map(r, c, matrix):
    count = 0
    if 0 <= r - 1 < r + 1 < len(matrix):
        if 0 <= c - 1 < c + 1 < len(matrix):
            back_slash = False # to check whether one arm of X is true
            forward_slash = False # to check whether other arm of X is true
            word = matrix[r-1][c-1] + matrix[r][c] + matrix[r+1][c+1]
            if word == 'MAS' or word == 'SAM':
                back_slash = True
            word = matrix[r-1][c+1] + matrix[r][c] + matrix[r+1][c-1]
            if word == 'MAS' or word == 'SAM':
                forward_slash = True
            if back_slash and forward_slash:
                count += 1
    return count

with open("data") as file:
    content = file.readlines()

# create a character matrix out of file input
data_matrix = []
for line in content:
    data_matrix.append([char for char in line.strip()])

xmas_count = 0 # counter for part 1
mas_count = 0 # counter for part 2
for row in range(len(data_matrix)):
    for col in range(len(data_matrix[0])):
        # for part 1, we have to find the work XMAS
        if data_matrix[row][col] == 'X':
            xmas_count += xmas_word_map(row, col, data_matrix)
        # for part 2, we have to find word MAS in the form of X
        if data_matrix[row][col] == 'A':
            mas_count += mas_word_map(row, col, data_matrix)

print('Part 1. XMAS count = ', xmas_count)
print('Part 2. X-MAS count = ', mas_count)