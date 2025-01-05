import re, sys

# function taking total time and distance as input
# and calculates all possible combinations
# returning the total winning ways
def find_winning_ways(total_time, record_distance):
    win_count = 0
    for press_time in range(total_time + 1):
        race_time = total_time - press_time
        total_distance = race_time * press_time
        if total_distance > record_distance:
            win_count += 1
    return win_count


# function which modifies input based on part 1 and part 2
# and returns the respective total winning ways
def calculate_total_winning_ways(is_part_2=False):
    with open("data") as file:
        content = file.readlines()

    data = []
    for line in content:
        data.append([int(value) for value in re.findall(r"\d+", line)])

    if is_part_2:
        # for part 2, just join all numbers
        # to get total time and distance
        total_time = int("".join([str(char) for char in data[0]]))
        total_distance = int("".join([str(char) for char in data[1]]))
        total_ways = find_winning_ways(total_time, total_distance)
    else:
        total_ways = 1
        for n in range(len(data[0])):
            total_ways *= find_winning_ways(data[0][n], data[1][n])
    return total_ways

print("Part 1. Total number of ways to beat the record = ", calculate_total_winning_ways())
print("Part 2. Total number of ways to beat the record (longer race) = ", calculate_total_winning_ways(True))