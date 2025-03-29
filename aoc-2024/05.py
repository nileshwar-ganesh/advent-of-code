with open("d1") as file:
    content = file.readlines()

# split ordering rules and updates
ordering_rules = {}
updates = []
# counter to add middle pages in both updates
sum_middle_pages = 0
sum_corrected_middle_pages = 0
for line in content:
    # check whether it is a ordering specifier
    if "|" in line:
        x, y = line.strip().split("|")
        if x not in ordering_rules.keys():
            ordering_rules[x] = [y]
        else:
            ordering_rules[x].append(y)
    elif len(line.strip()) > 0:
        # save all update entries in an array
        updates.append([x for x in line.strip().split(",")])
# process every update
for update in updates:
    wrong_order = False
    for idx, val in enumerate(update):
        for _, v in enumerate(update[0: idx]):
            if val in ordering_rules.keys():
                # if a value before the current value appears in dictionary, it means
                # that the ordering is false. mark the update as wrong and then
                # proceed to set it in the correct order
                if v in ordering_rules[val]:
                    wrong_order = True
                    first_part = update[0: idx + 1]
                    first_part.remove(v)
                    last_part = update[idx + 1:]
                    update = first_part + [v] + last_part
    if not wrong_order:
        # if initial update was in the right order, add for part 1 solution
        sum_middle_pages += int(update[int(len(update)/2)])
    else:
        # if not, add for part 2 of the solution
        sum_corrected_middle_pages += int(update[int(len(update) / 2)])

print("Part 1. Sum of all middle pages in correct update = ", sum_middle_pages)
print("Part 2. Sum of all middle pages in corrected update = ", sum_corrected_middle_pages)

