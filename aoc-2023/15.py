import re

with open("d1") as file:
    content = file.readlines()

def hash_algorithm(expression):
    value = 0
    for char in expression:
        # ascii code of current character
        value += ord(char)
        # multiply by 17
        value *= 17
        # remainder of division by 256
        value %= 256
    return value

for line in content:
    sequence = [expression for expression in line.strip().split(',')]

sum_hash = 0
boxes = [{} for _ in range(256)]
for expression in sequence:
    # part 1
    sum_hash += hash_algorithm(expression)
    # part 2
    values = re.findall(r"\w+", expression)
    if len(values) > 1:
        label, focal_length = values[0], values[1]
    else:
        label, focal_length = values[0], None
    index = hash_algorithm(label)
    if focal_length is None:
        if label in boxes[index].keys():
            boxes[index].pop(label)
        continue
    boxes[index][label] = focal_length

sum_lens_config = 0
for box_num, box in enumerate(boxes):
    for lens_pos, lens in enumerate(box.keys()):
        sum_lens_config += (box_num + 1) * (lens_pos + 1) * int(box[lens])

print("Part 1. Total sum of hash values = ", sum_hash)
print("Part 2. Total sum of lens configuration = ",sum_lens_config)


