def binary_to_decimal(number):
    result = 0
    for pos, num in enumerate(str(number)):
        result += int(num) * 2 ** (len(str(number)) - 1 - pos)
    return result

with open("data") as file:
    content = file.readlines()

wires = {}
operations = []
is_operations = False
for line in content:
    if line == "\n":
        is_operations = True
        continue
    if is_operations:
        operations.append(line.strip())
    else:
        wire, value = line.strip().split(':')
        wires[wire] = int(value)

while len(operations) > 0:
    instruction = operations.pop(0)
    w1, gate, w2, _ , w3 = instruction.split(' ')
    if w1 in wires.keys() and w2 in wires.keys():
        if gate == 'AND':
            if wires[w1] == 1 and wires[w2] == 1:
                wires[w3] = 1
            else:
                wires[w3] = 0
        if gate == 'OR':
            if wires[w1] == 1 or wires[w2] == 1:
                wires[w3] = 1
            else:
                wires[w3] = 0
        if gate == 'XOR':
            print(instruction)
            if wires[w1] == wires[w2]:
                wires[w3] = 0
            else:
                wires[w3] = 1
    else:
        operations.append(instruction)


wire = "z00"
result = ""
counter = 0
while True:
    if counter < 10:
        wire = "z0" + str(counter)
    else:
        wire = "z" + str(counter)
    if wire not in wires.keys():
        break
    result = str(wires[wire]) + result
    counter += 1

print(wires)
print(operations)
print(result)
print(binary_to_decimal(result))
