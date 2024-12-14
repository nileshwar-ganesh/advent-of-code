import re

def navigate(position, velocity, steps):
    global final_positions
    if steps == 0:
        final_positions.append(position)
        return position
    else:
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
        navigate((c, r), velocity, steps - 1)


with open("data") as file:
    content = file.readlines()

# creating a readable matrix out of input data
robots = []
tile_width = 101
tile_height = 103
final_positions = []
for line in content:
    values = re.findall(r"-?\d+", line)
    robots.append([(int(values[0]), int(values[1])), (int(values[2]), int(values[3]))])

for robot in robots:
    navigate(robot[0], robot[1], 100)

top_left = 0
top_right = 0
bot_left = 0
bot_right = 0
for position in final_positions:
    if 0 <= position[1] < (tile_height // 2) and 0 <= position[0] < (tile_width // 2):
        top_left += 1
    if (tile_height // 2) < position[1] < tile_height and 0 <= position[0] < (tile_width // 2):
        bot_left += 1
    if 0 <= position[1] < (tile_height // 2) and (tile_width // 2) < position[0] < tile_width:
        top_right += 1
    if (tile_height // 2) < position[1] < tile_height and (tile_width // 2) < position[0] < tile_width:
        bot_right += 1


print(top_left, top_right, bot_left, bot_right)
print(top_left * top_right * bot_left * bot_right)
