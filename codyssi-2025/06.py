def find_uncorrupted_value(char):
    if 65 <= ord(char) <= 90:
        return ord(char) - 38
    if 97 <= ord(char) <= 122:
        return ord(char) - 96


def convert_corrupted_character(previous_value):
    value = previous_value * 2 - 5
    if 1 <= value <= 52:
        return value
    elif value < 1:
        while not 1 <= value <= 52:
            value += 52
        return value
    elif value > 52:
        while not 1 <= value <= 52:
            value -= 52
        return value

with open("../data-files/d2") as file:
    content = file.readlines()

total_value_all = 0
value = None
for line in content:
    alphabets = [char for char in line.strip() if char.isalpha()]
    for index, char in enumerate(line.strip()):
        if char.isalpha():
            value = find_uncorrupted_value(char)
            total_value_all += value
            continue
        value = convert_corrupted_character(value)
        total_value_all += value

total_value_uncorrupted = 0
for char in alphabets:
    total_value_uncorrupted += find_uncorrupted_value(char)

print(len(alphabets))
print(total_value_uncorrupted)
print(total_value_all)





