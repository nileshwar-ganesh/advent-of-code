import re

with open("d1") as file:
    content = file.readlines()

def analyze_cubes(data, is_part_2=False):
    total = 0
    for line in data:
        game, draws = line.strip().split(":")
        id = int(re.findall(r"\d+", game)[0])
        is_valid_game = True
        if is_part_2:
            count_map = {"red": 0, "green": 0, "blue": 0}
        else:
            count_map = {"red": 12, "green": 13, "blue": 14}
        for draw in draws.split(";"):
            for cube in draw.split(","):
                count, color = cube.strip().split(" ")
                if int(count) > count_map[color]:
                    if is_part_2:
                        count_map[color] = int(count)
                    else:
                        is_valid_game = False
                        break
            if not is_valid_game:
                break
        if not is_part_2:
            if is_valid_game:
                total += id
        else:
            prod = 1
            for key, value in count_map.items():
                prod *= value
            total += prod
    return total

print(analyze_cubes(content))
print(analyze_cubes(content, True))

