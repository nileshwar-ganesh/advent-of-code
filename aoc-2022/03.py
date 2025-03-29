
def priority_value(char):
    if ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38

with open("d1") as file:
    content = file.readlines()

total = 0
line_nr = 0
badge_total = 0
group = []
for line in content:
    line_nr += 1
    line = line.strip()
    mid_point = int(len(line) / 2)
    compartment_1, compartment_2 = line[:mid_point], line[mid_point:]
    for char in list(set(compartment_1) & set(compartment_2)):
        total += priority_value(char)
    group.append(line)
    if line_nr == 3:
        for char in list(set(group[0]) & set(group[1]) & set(group[2])):
            badge_total += priority_value(char)
        line_nr = 0
        group = []

print("Part 1. The sum of the priorities of common items in compartments = ", total)
print("Part 2. The sum of the priorities of badges of Elf groups = ", badge_total)



