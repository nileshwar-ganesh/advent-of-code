with open("data") as file:
    content = file.readlines()

locks = []
keys = []
count = [-1, -1 , -1, -1, -1]
is_key = False
new_item = True
for line in content:
    if line == "\n":
        if is_key:
            keys.append(count)
        else:
            locks.append(count)
        count = [-1, -1 , -1, -1, -1]
        new_item = True
        continue
    if "." in line and new_item:
        is_key = True
        new_item = False
    if "." not in line and new_item:
        is_key = False
        new_item = False
    for pos, char in enumerate(line.strip()):
        if char == '#':
            count[pos] += 1

if is_key:
    keys.append(count)
else:
    locks.append(count)

fit_count = 0
for key in keys:
    for lock in locks:
        overlap = False
        for i in range(len(lock)):
            if lock[i] + key[i] >= 6:
                overlap = True
                break
        if not overlap:
            print(lock, key)
            fit_count += 1

print(keys)
print(locks)
print(fit_count)


