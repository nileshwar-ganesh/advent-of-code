import sys
sys.setrecursionlimit(10**6)

with open("data") as file:
    content = file.readlines()

lan_map = {}
t_map = []
for line in content:
    c1, c2 = line.strip().split("-")
    if c1[0] == "t" and c1 not in t_map:
        t_map.append(c1)
    if c2[0] == "t" and c2 not in t_map:
        t_map.append(c2)
    if c1 not in lan_map.keys():
        lan_map[c1] = [c2]
    else:
        if c2 not in lan_map[c1]:
            lan_map[c1].append(c2)
    if c2 not in lan_map.keys():
        lan_map[c2] = [c1]
    else:
        if c1 not in lan_map[c2]:
            lan_map[c2].append(c1)

interconnections = []
for key1 in lan_map.keys():
    for key2 in lan_map.keys():
        if key1 == key2:
            continue
        if key1 in lan_map[key2] and key2 in lan_map[key1]:
            common = list(set(lan_map[key1]) & set(lan_map[key2]))
            for c in common:
                if sorted([key1, key2, c]) not in interconnections:
                    interconnections.append(sorted([key1, key2, c]))
print(lan_map)
print(interconnections)
print(len(interconnections))

count = 0
for entry in interconnections:
    if len(list(set(entry) & set(t_map))) > 0:
        count += 1
print(count)


