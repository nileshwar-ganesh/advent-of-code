import copy
import re

with open("../data-files/d2") as file:
    content = file.readlines()

dataset = 0
frequencies = []
swap_order = []
test_index = None
for line in content:
    if line == '\n':
        dataset += 1
        continue
    if dataset == 0:
        frequencies.append(int(line.strip()))
    if dataset == 1:
        swap_order.append([int(value) for value in line.strip().split('-')])
    if dataset == 2:
        test_index = int(line.strip())

print(frequencies)
print(swap_order)
print(test_index)

frequencies_copy = copy.deepcopy(frequencies)
for i,j in swap_order:
    frequencies[i-1], frequencies[j-1] = frequencies[j-1], frequencies[i-1]

frequencies = copy.deepcopy(frequencies_copy)
for pos, value in enumerate(swap_order):
    i, j = value
    if pos == len(swap_order) - 1:
        k = swap_order[0][0]
    else:
        k = swap_order[pos + 1][0]

    frequencies[i - 1], frequencies[j - 1], frequencies[k - 1] = frequencies[k - 1], frequencies[i - 1], frequencies[j - 1]

frequencies = copy.deepcopy(frequencies_copy)
for i, j in swap_order:
    block_length = min(max(i, j) - min(i, j), len(frequencies) - max(i, j) + 1)
    for k in range(block_length):
        frequencies[i + k - 1], frequencies[j + k - 1] = frequencies[j + k - 1], frequencies[i + k - 1]

print(frequencies[test_index - 1])

