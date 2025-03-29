import re

def compare_cards(hand1, hand2, rank):
    for i in range(len(hand1)):
        if hand1[i] == hand2[i]:
            continue
        else:
            if rank.index(hand1[i]) > rank.index(hand2[i]):
                return True
            else:
                return False


def calculate_score(is_part_2=False):
    hand_group = {}
    hand_bid_map = {}
    for line in content:
        hand, bid = line.strip().split(' ')
        hand_bid_map[hand] = int(bid)
        hand_type = "".join([str(val) for val in sorted([hand.count(card) for card in set(hand)])])
        # part 2 starts
        if is_part_2:
            max_count = max([hand.count(char) if char != "J" else 0 for char in hand])
            j_count = hand.count("J")
            if j_count > 0 and max_count > 0:
                hand_type = hand_type.replace(str(j_count), '', 1)
                hand_type = hand_type[:-1] + str(int(hand_type[-1]) + j_count)
        hand_type = int(hand_type)
        # part 2 ends
        if hand_type not in hand_group.keys():
            hand_group[hand_type] = [hand]
        else:
            hand_group[hand_type].append(hand)

    hand_types = sorted([int(char) for char in hand_group.keys()], reverse=True)
    if is_part_2:
        rank = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    else:
        rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    ranked_hands = []
    for hand_type in hand_types:
        type_ranked_hands = []
        for unranked_hand in hand_group[hand_type]:
            if len(type_ranked_hands) == 0:
                type_ranked_hands.append(unranked_hand)
            elif len(type_ranked_hands) == 1:
                if compare_cards(type_ranked_hands[0], unranked_hand, rank):
                    type_ranked_hands.append(unranked_hand)
                else:
                    type_ranked_hands.insert(0, unranked_hand)
            else:
                for index in range(len(type_ranked_hands)):
                    if compare_cards(type_ranked_hands[index], unranked_hand, rank):
                        continue
                    else:
                        type_ranked_hands.insert(index, unranked_hand)
                        break
                if unranked_hand not in type_ranked_hands:
                    type_ranked_hands.append(unranked_hand)

        for card in type_ranked_hands:
            ranked_hands.append(card)

    total = 0
    rank = 1
    for card in ranked_hands:
        total += rank * hand_bid_map[card]
        rank += 1
    return total


with open("d1") as file:
    content = file.readlines()

print("Part 1. Total winnings = ", calculate_score())
print("Part 2. New total winnings = ", calculate_score(True))

