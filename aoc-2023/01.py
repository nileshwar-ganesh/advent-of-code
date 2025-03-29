import re

with open("d1") as file:
    content = file.readlines()

def find_calibration_values(data, is_part_2=False):
    # creating a number map, because the numbers may share a letter
    # e.g. oneight, where 'e' is shared by one and eight
    # a simple replace will either make it on8 or 1ight
    number_map = {'one': 'o1e', 'two': 't2o', 'three': 't3e',
                  'four': 'f4r', 'five': 'f5e', 'six': 's6x',
                  'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
    total = 0
    for line in data:
        line = line.strip()
        if is_part_2:
            # for part two, we also consider numbers which are spelled
            for key, value in number_map.items():
                line = re.sub(key, value, line)
        numbers = re.findall(r"\d", line)
        total += int(numbers[0] + numbers[-1])

    return total

print('Part 1. Sum of all of the calibration values = ', find_calibration_values(content))
print('Part 2. Sum of all of the calibration values = ', find_calibration_values(content, True))

