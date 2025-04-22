def reduce_line(line, is_part_3=False):
    i = 0
    while i < len(line):
        #print(line, i, len(line) - 1)
        if i == len(line) - 1 :
            return line
        is_numeric = False
        is_character = False
        string = line[i:i+2]
        for char in string:
            if char.isnumeric() :
                is_numeric = True
            elif char.isalpha() and is_part_3:
                is_character = True
            elif not is_part_3:
                is_character = True
        if is_numeric and is_character:
            line = line.replace(string, "", 1)
            i = max(0, i-1)
        else:
            i += 1

with open("../data-files/d2") as file:
    content = file.readlines()

alphabet_count = 0
for line in content:
    for char in line.strip():
        if char.isalpha():
            alphabet_count += 1

#print(alphabet_count)

total = 0
for line in content:
    line = reduce_line(line.strip(), True)
    if line:
        total += len(line)
print(total)

line = "ab213cd43c5fd"
#print(line.replace("3c", "", 1))
#print(line[1:3])
