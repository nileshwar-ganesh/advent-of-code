# The initial implementation with itertools ran out of memory with actual data
# This is referenced from the implementation of Jonathan Paulson

with open("data") as file:
    content = file.readlines()

matrix = []
max_length = 0
for line in content:
    test_value, numbers = line.strip().split(":")
    numbers = [int(i) for i in numbers.strip().split()]
    if len(numbers) > max_length:
        max_length = len(numbers)
    matrix.append([int(test_value), numbers])

def is_valid(target, ns, p2):
    if len(ns) == 1:
        return ns[0]==target
    if is_valid(target, [ns[0]+ns[1]] + ns[2:], p2):
        return True
    if is_valid(target, [ns[0]*ns[1]] + ns[2:], p2):
        return True
    if p2 and is_valid(target, [int(str(ns[0])+str(ns[1]))] + ns[2:], p2):
        return True
    return False

p1=0
p2=0
for entry in matrix:
    target, ns = entry[0], entry[1]
    if is_valid(target, ns, p2=False):
        p1 += target
    if is_valid(target, ns, p2=True):
        p2 += target

print(p1)
print(p2)

