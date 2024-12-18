import re

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

with open("data") as file:
    content = file.readlines()

registry = {}
program = []
# creating a readable matrix out of input data
for line in content:
    if "Register A" in line:
        registry["A"] = int(re.findall(r"\d+", line)[0])
    if "Register B" in line:
        registry["B"] = int(re.findall(r"\d+", line)[0])
    if "Register C" in line:
        registry["C"] = int(re.findall(r"\d+", line)[0])
    if "Program" in line:
        program =[int(char) for char in re.findall(r"\d+", line)]

print(registry)
print(program)
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
print(",".join(result))