from pyperclip import is_available

with open("d1") as file:
    content = file.readlines()

def find_design(patterns, design):
    if design == "":
        return 1
    if design in design_map.keys():
        return design_map[design]
    combinations = 0
    for pattern in patterns:
        if pattern == design[0:len(pattern)]:
            combinations += find_design(patterns, design[len(pattern):])
    design_map[design] = combinations
    return combinations

is_design = False
patterns = []
designs = []
design_map = {}
for line in content:
    if line == "\n":
        is_design = True
        continue
    if not is_design:
        patterns = [char.strip() for char in line.strip().split(",")]
    else:
        designs.append(line.strip())

total = 0

for design in designs:
    total += find_design(patterns, design)
print(total)
