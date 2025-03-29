import copy

# recursive function which generates the sub-arrays of difference
def calculate_difference(array):
    if len(array) == 2:
        return [array[1] - array[0]]
    else:
        return [array[1] - array[0]] + calculate_difference(array[1:])

# recursive function utilizes the previous one and finds all steps till zero array
def calculate_steps(array):
    if array.count(0) == len(array):
        return [array]
    else:
        difference = calculate_difference(array)
        return [array] + calculate_steps(difference)

# to extrapolate a step in forward direction
def extrapolate_forward(array):
    values = array.pop(0)
    if len(array) == 0:
        value = values[-1]
    else:
        value = values[-1] + extrapolate_forward(array)
    return value

# to extrapolate a step in backward direction
def extrapolate_backward(array):
    values = array.pop(0)
    if len(array) == 0:
        value = values[0]
    else:
        value = values[0] - extrapolate_backward(array)
    return value

with open("d1") as file:
    content = file.readlines()

historical_values = []
for line in content:
    historical_values.append([int(n) for n in line.strip().split(' ')])

total_f = 0
total_b = 0
for value_set in historical_values:
    value_ladder = calculate_steps(value_set)
    extrapolated_value = extrapolate_backward(copy.deepcopy(value_ladder))
    total_b += extrapolated_value
    extrapolated_value = extrapolate_forward(copy.deepcopy(value_ladder))
    total_f += extrapolated_value

print("Part 1. Sum of extrapolated values (forward) = ", total_f)
print("Part 2. Sum of extrapolated values (backward) = ", total_b)