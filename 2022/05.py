import copy
import re

def run_instructions(instructions, stack, is_part_2=False):
    for instruction in instructions:
         moved_crates = []
         for _ in range(instruction[0]):
            if is_part_2:
                moved_crates.insert(0, stack[instruction[1]].pop(-1))
            else:
                moved_crates.append(stack[instruction[1]].pop(-1))
         for crate in moved_crates:
             stack[instruction[2]].append(crate)

    string = ""
    for i in range(len(stack.keys())):
        string += stack[i + 1][-1]

    return string

with open("data") as file:
    content = file.readlines()

stack = {}
is_instruction = False
instructions = []
for line in content:
    if line == "\n":
        is_instruction = True
        continue
    if is_instruction:
        instructions.append([int(value) for value in re.findall(r"\d+", line)])
        continue
    s = 1
    for i in range(0, len(line), 4):
        char = re.findall(r"\w", line[i:i+4])
        if len(char) > 0 and not char[0].isnumeric():
            if s not in stack.keys():
                stack[s] = char
            else:
                stack[s].insert(0, char[0])
        s += 1

print("Part 1. Top crates after rearrangement (one by one) = ", run_instructions(instructions, copy.deepcopy(stack)))
print("Part 2. Top crates after rearrangement (in a set) = ", run_instructions(instructions, copy.deepcopy(stack), True))
