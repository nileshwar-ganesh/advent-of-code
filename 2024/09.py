with open("example") as file:
    content = file.readlines()

# creating a readable matrix out of input data
line_data = []
for line in content:
    line_data = [int(char) for char in line.strip()]

number = 0
number_array = []
blank_array = []
for index, entry in enumerate(line_data):
    if index % 2 == 0:
        number_array.append([number] * entry)
        number += 1
    else:
        blank_array.append(entry)
print(number_array)
print(blank_array)