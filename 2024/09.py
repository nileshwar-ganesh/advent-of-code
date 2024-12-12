import math
import sys

with open("data") as file:
    content = file.readlines()

# creating a readable matrix out of input data
line_data = []
for line in content:
    line_data = [int(char) for char in line.strip()]

print(len(line_data))
number = 0
number_array = []
blank_array = []
occupied_slots = 0
for index, entry in enumerate(line_data):
    if index % 2 == 0:
        concat_string = [number] * entry
        # while len(concat_string) < entry:
        #    concat_string += str(number)
        number_array.append(concat_string)
        occupied_slots += entry
        number += 1
    else:
        blank_array.append(entry)

answer = []
while len(number_array) > 0:
    for num in number_array.pop(0):
        answer.append(num)
    if len(number_array) <= 0:
        break
    blank_spaces = blank_array.pop(0)
    tail = []
    for _ in range(blank_spaces):
        if len(number_array) <= 0:
            break
        if len(tail) == 0:
            tail = number_array.pop(-1)
        answer.append(tail.pop(-1))
    if len(tail) > 0:
        number_array.append(tail)

total_value = 0
for index, value in enumerate(answer):
    total_value += index * int(value)


print(answer)
print(total_value)


