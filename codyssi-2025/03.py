import re

with open("../data-files/d2") as file:
    content = file.readlines()

box_data = []
for line in content:
    numbers = [int(num) for num in re.findall(r'\d+', line)]
    box_data.append(numbers)

total_boxes = 0
corrected_total_boxes = 0
previous_pile = []
max_unique_boxes = float('-inf')
for data in box_data:
    boxes = []
    for i in range(0, len(data), 2):
        total_boxes += data[i + 1] - data[i] + 1
        boxes += [int(num) for num in range(data[i], data[i + 1] + 1)]
    corrected_total_boxes += len(set(boxes))
    if not previous_pile:
        previous_pile = boxes
        continue
    unique_boxes = set(boxes + previous_pile)
    if len(unique_boxes) > max_unique_boxes:
        max_unique_boxes = len(unique_boxes)
    previous_pile = boxes


print('Part 1. Total number of boxes in all piles = ', total_boxes)
print('Part 2. Total number of boxes in all piles (removing duplicates) = ', corrected_total_boxes)
print('Part 3. Maximum number of unique boxes in adjacent piles = ', max_unique_boxes)

