# The initial implementation with itertools ran out of memory with actual data
# Implemented after studying the solution of Jonathan Paulson

with open("data") as file:
    content = file.readlines()

# convert input data into a matrix
matrix = []
for line in content:
    test_value, numbers = line.strip().split(":")
    numbers = [int(i) for i in numbers.strip().split()]
    matrix.append([int(test_value), numbers])

# recursive function, which goes through all elements in the number list
# and compares the end result of operation with test value
def validity_check(test_value, numbers, is_part_2):
    # if only one element left, check whether the total matches test value
    if len(numbers) == 1:
        return numbers[0] == test_value
    # else, go both ways for part 1: addition and multiplication
    if validity_check(test_value, [numbers[0] + numbers[1]] + numbers[2:], is_part_2):
        return True
    if validity_check(test_value, [numbers[0] * numbers[1]] + numbers[2:], is_part_2):
        return True
    # for part 2, introduce concatenation operator as well
    if is_part_2 and validity_check(test_value, [int(str(numbers[0])+str(numbers[1]))] + numbers[2:], is_part_2):
        return True

total_calibration_1 = 0
total_calibration_2 = 0
for entry in matrix:
    test_value, numbers = entry[0], entry[1]
    if validity_check(test_value, numbers, is_part_2=False):
        total_calibration_1 += test_value
    if validity_check(test_value, numbers, is_part_2=True):
        total_calibration_2 += test_value

print("Part 1. Total calibration (for operators + and *) = ", total_calibration_1)
print("Part 2. Total calibration (for operators +, * and ||) = ", total_calibration_2)
