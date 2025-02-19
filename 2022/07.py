with open("data") as file:
    content = file.readlines()

directory_map = {}
directories = set()
files = {}
directory_trail = []
directory_size = {}
file_size = 0
for line in content:
    line = line.strip()
    if "$ cd" in line:
        _, _, name = line.split()
        if name == '..':
            key = "-".join(directory_trail)
            child = directory_size[key]
            directory_trail.pop()
            key = "-".join(directory_trail)
            directory_size[key] += child
            continue
        directory_trail.append(name)
        key = "-".join(directory_trail)
        if key not in directory_size.keys():
            directory_size[key] = 0
            continue
    if "$ ls" in line or "dir" in line:
        continue
    size, name = line.split(' ')
    directory_size[key] += int(size)

print(directory_size)

sizes = [value for key, value in directory_size.items()]
total = 0
for value in sorted(sizes):
    if value <= 100000:
        total += value

print(total)