import re

def apply_pricing_function(quality, add_value, mul_value, exp_value):
    price = quality ** exp_value
    price *= mul_value
    price += add_value
    return price

with open("../data-files/d2") as file:
    content = file.readlines()

room_qualities = []
function_values = []
is_room_quality = False
for line in content:
    if "Function" in line:
        if "ADD" in line:
            numbers = re.findall(r"\d+", line)
            function_values.append(int(numbers[0]))
        if "multiply".upper() in line:
            numbers = re.findall(r"\d+", line)
            function_values.append(int(numbers[0]))
        if "raise".upper() in line:
            numbers = re.findall(r"\d+", line)
            function_values.append(int(numbers[0]))
    if line == "\n":
        is_room_quality = True
        continue
    if is_room_quality:
        room_qualities.append(int(line.strip()))

median = sorted(room_qualities)[len(room_qualities) // 2]
median_price = apply_pricing_function(median, function_values[0], function_values[1], function_values[2])
print("Part 1. Median price = ", median_price)

even_qualities = [quality for quality in room_qualities if quality % 2 == 0]
total_price = apply_pricing_function(sum(even_qualities), function_values[0], function_values[1], function_values[2])
print("Part 2. Total price of even qualities = ", total_price)

budget = 15000000000000
min_difference = float('inf')
top_quality = None
for quality in room_qualities:
    price = apply_pricing_function(quality, function_values[0], function_values[1], function_values[2])
    if 0 < budget - price < min_difference:
        min_difference = budget - price
        top_quality = quality

print("Part 3. Highest quality for available budget = ", top_quality)




print()
