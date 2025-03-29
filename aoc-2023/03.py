import re, sys

with open("d1") as file:
    content = file.readlines()

# convert input into a matrix
grid = []
for line in content:
    values = [char for char in line.strip()]
    grid.append(values)

row = 0
symbol_map = {}  # stores the location of symbols and the numbers around it
mask = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for line in grid:
    number = ""
    columns = ""
    symbol_positions = set()
    # for each line, start reading the number first
    # also look for a symbol adjacent to it
    for col, value in enumerate(line):
        # if the value is not numeric, it means reading the number has ended
        # so we can store the location of the numbers
        if not value.isnumeric():
            for location in symbol_positions:
                if location not in symbol_map.keys():
                    symbol_map[location] = [(row, columns, number)]
                else:
                    symbol_map[location].append((row, columns, number))
            # clear the location and d1 holding variables
            number = ""
            columns = ""
            symbol_positions = set()
            continue
        # if it is a number, than start reading and storing the digits
        number += value
        columns += str(col)
        # run a mask square around the location to check whether it has any symbols
        for entry in mask:
            r = row + entry[0]
            c = col + entry[1]
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if not grid[r][c].isnumeric() and not grid[r][c] == '.':
                    symbol_positions.add((r, c))
    # if a line ends with a number, then we need to store this one as well
    if len(symbol_positions) > 0:
        for location in symbol_positions:
            if location not in symbol_map.keys():
                symbol_map[location] = [(row, columns, number)]
            else:
                symbol_map[location].append((row, columns, number))
    row += 1

# calculation of results
sum_part_numbers = 0
sum_gear_ratios = 0
for key, value in symbol_map.items():
    is_gear = False
    product = 1
    for val in value:
        # part number is sum of all numbers adjacent to a symbol
        sum_part_numbers += int(val[2])
        if grid[key[0]][key[1]] == "*" and len(value) > 1:
            is_gear = True
            # gear ratio is calculated if there are more than one numbers
            # adjacent to symbol '*'
            product *= int(val[2])
    if is_gear:
        # and sum up the gear ratios, if a gear pair is found
        sum_gear_ratios += product

print('Part 1. Sum of part numbers = ', sum_part_numbers)
print('Part 2. Sum of gear ratios = ', sum_gear_ratios)