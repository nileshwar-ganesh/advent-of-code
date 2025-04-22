import re

def find_manhattan_distance(coordinate_1, coordinate_2):
    return abs(coordinate_1[0] - coordinate_2[0]) + abs(coordinate_1[1] - coordinate_2[1])

with open("../data-files/d2") as file:
    content = file.readlines()

coordinates = []
for line in content:
    values = line.strip().replace('(', '').replace(')', '').split(',')
    coordinates.append(tuple([int(num) for num in values]))

max_distance = float('-inf')
min_distance = float('inf')
closest_island = None
for coordinate in coordinates:
    distance = find_manhattan_distance(coordinate, (0, 0))
    if distance < min_distance:
        min_distance = distance
        closest_island = coordinate
    if distance > max_distance:
        max_distance = distance
distance_farthest_closest = max_distance - min_distance

islands = []
min_distance = float('inf')
for coordinate in coordinates:
    if coordinate == closest_island:
        continue
    distance = find_manhattan_distance(coordinate, closest_island)
    if distance < min_distance:
        min_distance = distance
        islands = [coordinate]
    elif distance == min_distance:
        islands.append(coordinate)

total_distance = find_manhattan_distance(closest_island, (0, 0))
while coordinates:
    if len (coordinates) == 1:
        break
    index = coordinates.index(closest_island)
    coordinates.pop(index)
    islands = []
    min_distance = float('inf')
    for coordinate in coordinates:
        if coordinate == closest_island:
            continue
        distance = find_manhattan_distance(coordinate, closest_island)
        if distance < min_distance:
            min_distance = distance
            islands = [coordinate]
        elif distance == min_distance:
            islands.append(coordinate)
    if len(islands) > 1:
        islands.sort(key=lambda x: x[0])
        if islands[0][0] == islands[0][1]:
            islands.sort(key=lambda x: x[1])
    total_distance += find_manhattan_distance(closest_island, islands[0])
    closest_island = islands[0]


print(distance_farthest_closest)
print(total_distance)
