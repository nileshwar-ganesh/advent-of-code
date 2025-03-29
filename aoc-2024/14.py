import copy
import re

def navigate_step():
    top_left = 0
    top_right = 0
    bot_left = 0
    bot_right = 0
    for robot in robots:
        position, velocity = robot[0], robot[1]
        r = position[1] + velocity[1]
        c = position[0] + velocity[0]
        if r < 0:
            r += tile_height
        if r >= tile_height:
            r = abs(r % tile_height)
        if c < 0:
            c += tile_width
        if c >= tile_width:
            c = abs(c % tile_width)

        if 0 <= r < (tile_height // 2) and 0 <= c < (tile_width // 2):
            top_left += 1
        if (tile_height // 2) < r < tile_height and 0 <= c < (tile_width // 2):
            bot_left += 1
        if 0 <= r < (tile_height // 2) and (tile_width // 2) < c < tile_width:
            top_right += 1
        if (tile_height // 2) < r < tile_height and (tile_width // 2) < c < tile_width:
            bot_right += 1

        robot[0] = (c, r)

    return top_left * top_right * bot_left * bot_right


with open("d1") as file:
    content = file.readlines()

# creating a readable matrix out of input d1
robots = []
tile_width = 101
tile_height = 103
final_positions = []
for line in content:
    values = re.findall(r"-?\d+", line)
    robots.append([(int(values[0]), int(values[1])), (int(values[2]), int(values[3]))])

scores = []
for step in range(1, 10000):
    score = navigate_step()
    scores.append(score)
    if step == 100:
        print('Part 1. The safety factor after 100 seconds = ', score)

print('Part 2. Time taken to display easter egg = ', scores.index(min(scores)) + 1)
