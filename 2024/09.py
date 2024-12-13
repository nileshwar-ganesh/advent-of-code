import copy

# function which calculates the checksum value, iterating through answer
def calculate_total(answer):
    total = 0
    for pos, val in enumerate(answer):
        if val != ".":
            total += val * pos
    return total

# function which shuffles and arranges the ids into blank spaces
def arrange_ids(spaces, numbers, answer, is_part_2=False):
    for space in spaces:
        for number in reversed(numbers):
            # exit if cross over of indices happen
            if space[0] >= number[0]:
                break
            # if a id block is completely allocated, ignore it
            if number[1] == 0:
                continue
            # if id block fits into the vacant space, follow if condition
            if number[1] <= space[1]:
                for i in range(number[1]):
                    answer[space[0] + i] = number[2]
                    answer[number[0] + number[1] - (i + 1)] = '.'
                space[0] += number[1]
                space[1] -= number[1]
                number[1] = 0
            else:
                # for part 1, since the whole block of ids is not moved
                # we need to split the number blocks at the end, to fill gaps
                if not is_part_2:
                    for i in range(space[1]):
                        answer[space[0] + i] = number[2]
                        answer[number[0] + number[1] - (i + 1)] = '.'
                    number[1] -= space[1]
                    break
                # for part 2, since we are moving only if id blocks fit completely
                # the else part of the condition does not matter
                continue
    return calculate_total(answer)

with open("data") as file:
    content = file.readlines()

# creating a readable matrix out of input data
line_data = []
for line in content:
    line_data = [int(char) for char in line.strip()]


id = 0  # file id
idx = 0  # position in the array
spaces = []  # location and length details of space blocks
numbers = []  # location and length details of file id blocks
answer = []  # the array which will transform into the final solution
for index, entry in enumerate(line_data):
    if index % 2 == 0:
        numbers.append([idx, entry, id])
        for _ in range(entry):
            answer.append(id)
            idx += 1
        id += 1
    else:
        spaces.append([idx, entry])
        for _ in range(entry):
            answer.append(".")
            idx += 1

checksum = arrange_ids(copy.deepcopy(spaces), copy.deepcopy(numbers), copy.deepcopy(answer), False)
print("Part 1. File System Checksum = ", checksum)
checksum = arrange_ids(copy.deepcopy(spaces), copy.deepcopy(numbers), copy.deepcopy(answer), True)
print("Part 2. File System Checksum (reworked) = ", checksum)