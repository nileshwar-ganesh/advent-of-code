opponent = {'A': 'Z', 'B': 'X', 'C': 'Y'}
player = {'X': 'C', 'Y': 'A', 'Z': 'B'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
value = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}


with open("d1") as file:
    content = file.readlines()

score = 0
score_2 = 0
for line in content:
    opp_choice, pl_choice = line.strip().split(' ')

    # part 1
    if opponent[opp_choice] == pl_choice:
        score += value[pl_choice]
    elif player[pl_choice] == opp_choice:
        score += (value[pl_choice] + 6)
    elif draw[opp_choice] == pl_choice:
        score += (value[pl_choice] + 3)

    # part 2
    if pl_choice == 'X': # lose the round
        score_2 += value[opponent[opp_choice]]
    elif pl_choice == 'Y': # draw
        score_2 += (value[opp_choice] + 3)
    elif pl_choice == 'Z': # win the round
        for key, val in player.items():
            if val == opp_choice:
                score_2 += (value[key] + 6)

print("Part 1. Total score based on direct given selection = ", score)
print("Part 2. Total score after selecting based on given strategy = ",score_2)


