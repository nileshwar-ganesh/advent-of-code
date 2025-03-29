import copy
import re, sys
from itertools import permutations


def generate_combinations(numbers):
    # Convert each permutation tuple to an integer
    return [int(''.join(map(str, perm))) for perm in permutations(numbers)]

def OctalToDecimal(num):
    decimal_value = 0
    base = 1
    while (num):
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value

def values(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registry["A"]
    elif operand == 5:
        return registry["B"]
    elif operand == 6:
        return registry["C"]
    elif operand == 7:
        return 0

def operations(opcode, operand, pointer):
    value = None
    if opcode == 0:
        registry["A"] = registry["A"] // (2 ** values(operand))
    elif opcode == 1:
        registry["B"] = registry["B"] ^ operand
    elif opcode == 2:
        registry["B"] = values(operand) % 8
    elif opcode == 3:
        if registry["A"] != 0:
            return operand, value
    elif opcode == 4:
        registry["B"] = registry["B"] ^ registry["C"]
    elif opcode == 5:
        value = values(operand) % 8
    elif opcode == 6:
        registry["B"] = registry["A"] // (2 ** values(operand))
    elif opcode == 7:
        registry["C"] = registry["A"] // (2 ** values(operand))
    pointer += 2
    return pointer, value

with open("example") as file:
    content = file.readlines()

registry = {}
program = []
# creating a readable matrix out of input d1
for line in content:
    if "Register A" in line:
        registry["A"] = int(re.findall(r"\d+", line)[0])
    if "Register B" in line:
        registry["B"] = int(re.findall(r"\d+", line)[0])
    if "Register C" in line:
        registry["C"] = int(re.findall(r"\d+", line)[0])
    if "Program" in line:
        program =[int(char) for char in re.findall(r"\d+", line)]

generate_combinations([2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0])
sys.exit()

reg = copy.deepcopy(registry)
for i in set(generate_combinations([2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0])):
    registry = copy.deepcopy(reg)
    registry["A"] = OctalToDecimal(i)
    # print(program)
    pointer = 0
    result = []
    while True:
        opcode, operand = program[pointer], program[pointer + 1]
        pointer, value = operations(opcode, operand, pointer)
        if value != None:
            result.append(value)
        if pointer >= len(program):
            break

    result = [str(char) for char in result]

    print(OctalToDecimal(i), ",".join(result))

    if ",".join(result) == "2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0":
        print(i, OctalToDecimal(i))
        break
