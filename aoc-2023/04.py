import re

with open("d1") as file:
    content = file.readlines()

card_map = {}
total_points = 0
total_cards = 0
for line in content:
    # splitting the input line into card d1, winning hand and player hand
    card, numbers = line.strip().split(":")
    card_number = re.findall(r"\d+", card)[0]
    winning, player = numbers.split("|")
    winning_numbers = re.findall(r"\d+", winning)
    player_numbers = re.findall(r"\d+", player)

    # add the current card to card count
    if card_number not in card_map.keys():
        card_map[card_number] = 1
    else:
        card_map[card_number] += 1
    # add the final card count to total of scratch cards
    total_cards += card_map[card_number]

    # winning hand holds the overlapping d1
    winning_hand = list(set(winning_numbers) & set(player_numbers))
    # if any card has winning hands
    if len(winning_hand) > 0:
        # points in multiples of 2, starting from 1, 2, 4, ...
        point = 2 ** (len(winning_hand) - 1)
        total_points += point
    # for each winning number in card, add one card to subsequent cards
    # the current card may be more than one in number
    # hence add the total number of current card, to each subsequent cards
    for n in range(1, len(winning_hand) + 1):
        if str(int(card_number) + n) not in card_map.keys():
            card_map[str(int(card_number) + n)] = card_map[card_number]
        else:
            card_map[str(int(card_number) + n)] += card_map[card_number]

print('Part 1. Total worth in points = ', total_points)
print('Part 2. Total scratch cards = ', total_cards)