with open("d1") as file:
    content = file.readlines()

elfs = []
total_calories = 0
for line in content:
    if line == "\n":
        elfs.append(total_calories)
        total_calories = 0
        continue
    total_calories += int(line.strip())
elfs.append(total_calories)

print('Part 1. Total maximum calories carried by the Elf = ', max(elfs))
print('Part 2. Total calories carried by the top three Elves = ', sum(sorted(elfs, reverse=True)[0:3]))
