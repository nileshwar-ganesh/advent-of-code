import re

with open("data") as file:
    content = file.readlines()

total_overlap = 0
total_fully_contained = 0
for line in content:
    sections = [int(value) for value in re.findall(r"\d+", line)]
    # overlap between assigned sections
    if sections[0] <= sections[2] and sections[1] >= sections[3]:
        # (A [0]-[1]) |-----------------------|
        # (B [2]-[3])   |-----------------|
        total_fully_contained += 1
        total_overlap += 1
    elif sections[2] <= sections[0] and sections[3] >= sections[1]:
        # (A [0]-[1])   |-----------------|
        # (B [2]-[3]) |-----------------------|
        total_fully_contained += 1
        total_overlap += 1
    elif sections[0] <= sections[2] <= sections[1] <= sections[3]:
        # (A [0]-[1]) |-----------------------|
        # (B [2]-[3])            |-----------------|
        total_overlap += 1
    elif sections[2] <= sections[0] <= sections[3] <= sections[1]:
        # (A [0]-[1])            |-----------------------|
        # (B [2]-[3]) |-----------------|
        total_overlap += 1

print("Part 1. Total assignment pairs, where one range fully contains the other = ", total_fully_contained)
print("Part 2. Total assignment pairs, where the ranges overlap = ", total_overlap)
