import numpy as np
with open("example") as file:
    content = file.readlines()

patterns = []
pattern = []
for line in content:
    if line == "\n":
        patterns.append(pattern)
        pattern = []
        continue
    pattern.append([char for char in line.strip()])
if pattern:
    patterns.append(pattern)

total = 0
for pattern in patterns:
    pattern = np.array(pattern)
    for row, values in enumerate(pattern):
        nr = min(len(pattern[:row + 1, :]), len(pattern[row + 1:, :]))
        if nr > 0:
            upper = np.array(pattern[row + 1 - nr:row + 1, :])
            lower = np.array(pattern[row+1:row+nr+1, :])
            if np.array_equal(upper, np.flipud(lower)):
                total += 100*(row+1)
                break

    for col in range(len(pattern[0])):
        nc = min(len(pattern[:, :col+1][0]), len(pattern[:, col + 1:][0]))
        if nc > 0:
            left = np.array(pattern[:, col + 1 - nc:col + 1])
            right = np.array(pattern[:, col + 1:col + nc + 1])
            if np.array_equal(left, np.fliplr(right)):
                total += (col + 1)
                break

print(total)