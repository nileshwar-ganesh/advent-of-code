with open("../data-files/d2") as file:
    content = file.readlines()


total_memory_units = 0
total_memory_units_compressed = 0
total_memory_units_lossless = 0
for line in content:
    line = line.strip()
    for char in set(line):
        total_memory_units += line.count(char) * (ord(char) - 64)

    n = len(line) // 10
    string = line[:n] + str(len(line) - 2*n) + line[len(line)-n:]
    for char in string:
        if char.isnumeric():
            total_memory_units_compressed += int(char)
            continue
        total_memory_units_compressed += (ord(char) - 64)


    string = ""
    current_char = ""
    char_count = 0
    for char in line:
        if current_char != char:
            if char_count > 0:
                string += str(char_count) + current_char
            current_char = char
            char_count = 1
            continue
        char_count += 1
    string += str(char_count) + current_char
    for char in string:
        if char.isnumeric():
            total_memory_units_lossless += int(char)
            continue
        total_memory_units_lossless += (ord(char) - 64)


print(total_memory_units)
print(total_memory_units_compressed)
print(total_memory_units_lossless)
