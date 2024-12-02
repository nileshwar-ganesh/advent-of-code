with open("data") as file:
    content = file.readlines()

left_list = []
right_list = []
for entry in content:
    val1, val2 = entry.strip().split()
    left_list.append(int(val1))
    right_list.append(int(val2))

left_list = sorted(left_list)
right_list = sorted(right_list)

total_distance = 0
similarity_score = 0
for idx in range(0, len(left_list)):
    total_distance += abs(left_list[idx] - right_list[idx])
    similarity_score += left_list[idx] * right_list.count(left_list[idx])

print("Part 1. Total Distance = ", total_distance)
print("Part 2. Similarity Score = ", similarity_score)