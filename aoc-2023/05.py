import re, sys

with open("d1") as file:
    content = file.readlines()

seeds = []
almanac = {"seed-to-soil":[],
            "soil-to-fertilizer": [],
            "fertilizer-to-water": [],
            "water-to-light": [],
            "light-to-temperature": [],
            "temperature-to-humidity": [],
            "humidity-to-location": []}
almanac_key = ""
for line in content:
    if "seeds" in line:
        seeds = [int(seed) for seed in re.findall(r"\d+", line)]
    for key in almanac.keys():
        if key in line:
            almanac_key = key
    if len(almanac_key) > 0 and not almanac_key in line and not line == "\n":
        data = [int(value) for value in re.findall(r"\d+", line)]
        almanac[almanac_key].append(data)


lowest_location_number = None
for value in seeds:
    for almanac_key, almanac_values in almanac.items():
        for values in almanac_values:
            total_range = values[2]
            source = values[1]
            destination = values[0]
            if source <= value < source + total_range:
                value = destination + (value - source)
                break
    if lowest_location_number is None:
        lowest_location_number = value
        continue
    if value < lowest_location_number:
        lowest_location_number = value

print(lowest_location_number)