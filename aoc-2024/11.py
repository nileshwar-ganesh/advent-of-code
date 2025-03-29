# The first part was implemented without any help, but was not optimal for part 2
# The current method is implemented after studying the solution of Jonathan Paulson

def split_stone(stone, blinks):
    # if the stone blink pair is already present, use it
    if (stone, blinks) in memory.keys():
        return memory[(stone, blinks)]
    # if no more blinks remain, the last stone does not split
    if blinks == 0:
        value = 1
    # if stone has value of 0, it becomes one for the next step and blinks - 1 steps remain
    elif stone == 0:
        value = split_stone(1, blinks - 1)
    # if stone even number of digits, it splits and blinks - 1 steps remain
    elif len(str(stone)) % 2 == 0:
        left = int(str(stone)[:len(str(stone)) // 2])
        right = int(str(stone)[len(str(stone)) // 2:])
        value = split_stone(left, blinks-1) + split_stone(right, blinks-1)
    # else, it gets multiplied by 2024
    else:
        value = split_stone(stone * 2024, blinks-1)
    # once you have a result, update it to memory
    memory[(stone, blinks)] = value
    return value

# read from d1 file
with open("d1") as file:
    content = file.readlines()

# this holds the d1 about already calculated stone - blink pair
memory = {}
for line in content:
    stones = [int(val) for val in line.strip().split()]

# go through each stone in the input list and then process one by one
def find_total_stones(stones, blinks=5):
    total_stones = 0
    for stone in stones:
        total_stones += split_stone(stone, blinks)
    return total_stones

print("Part 1. Stones after 25 blinks = ", find_total_stones(stones, 25))
print("Part 2. Stones after 75 blinks = ", find_total_stones(stones, 75))