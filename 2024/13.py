import re
with open("data") as file:
    content = file.readlines()

# creating a readable matrix out of input data
equations = []
data = []
for line in content:
    if line == "\n":
        continue
    else:
        values = re.findall(r"\d+", line)
        data.append((int(values[0]), int(values[1])))
        if "Prize" in line:
            equations.append(data)
            data = []

# solving system of two equations by elimination
cost_1 = 0
cost_2 = 0
for data in equations:
    # part 1
    numerator = (data[2][0] * data[0][1]) - (data[2][1] * data[0][0])
    denominator = (data[1][0] * data [0][1]) - (data[1][1] * data[0][0])
    if numerator % denominator == 0:
        y = int(numerator / denominator)
        x = 0
        if (data[2][0] - (data[1][0] * y)) % data[0][0] == 0:
            x = int((data[2][0] - (data[1][0] * y)) / data[0][0])
        if x != 0:
            cost_1 += 3*x + y
    # part 2: adding 10000000000000 to X and Y co-ordinates
    numerator = ((10000000000000 + data[2][0]) * data[0][1]) - ((10000000000000 + data[2][1]) * data[0][0])
    denominator = (data[1][0] * data[0][1]) - (data[1][1] * data[0][0])
    if numerator % denominator == 0:
        y = int(numerator / denominator)
        x = 0
        if ((10000000000000 + data[2][0]) - (data[1][0] * y)) % data[0][0] == 0:
            x = int(((10000000000000 + data[2][0]) - (data[1][0] * y)) / data[0][0])
        if x != 0:
            cost_2 += 3 * x + y

print("Part 1. Fewest tokens spent = ", cost_1)
print("Part 2. Fewest tokens spent (reworked) = ", cost_2)
