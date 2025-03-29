from math import gcd

with open("d1") as file:
    content = file.readlines()

is_data = False
instruction = ""
network = {}
start_keys = []
for line in content:
    if line == "\n":
        is_data = True
        continue
    if not is_data:
        instruction = line.strip()
    else:
        key, value = line.strip().split(" = ")
        network[key] = {'L': value[1:4], 'R': value[6:9]  }
        if key[-1] == "A":
            start_keys.append(key)


def calculate_steps(keys, is_part_2=False):
    if not is_part_2:
        keys = ['AAA']

    steps = []
    for key in keys:
        index = 0
        step = 0
        while True:
            if is_part_2:
                condition = (key[-1] != 'Z')
            else:
                condition = (key != 'ZZZ')
            if not condition:
                break
            if index == len(instruction):
                index = 0
            key = network[key][instruction[index]]
            index += 1
            step += 1
        steps.append(step)

    if not is_part_2:
        return steps[0]
    else:
        lcm = 1
        for step in steps:
            lcm = lcm * step // gcd(lcm, step)
        return lcm


print('Part 1. Steps required to reach ZZZ = ', calculate_steps(start_keys))
print('Part 1. Steps to simultaneously reach all nodes ending with Z = ', calculate_steps(start_keys, True))

