with open("d1") as file:
    content = file.readlines()

# create a 2D array out of input (reports and levels)
reports = []
for entry in content:
    reports.append([int(val) for val in entry.strip().split()])

# calculate for safe report counts
safe_count_1 = 0 # for the first part
safe_count_2 = 0 # for the second part
for report in reports:
    # starts with assumption that the report is not safe
    is_safe = False
    # creates a difference array out of adjacent elements
    difference = [report[i-1] - report[i] for i in range(1, len(report))]
    # checks whether there is a change in direction
    # basically counts the number of negative elements in the list
    # strictly descending array will have only positive elements
    # strictly increasing array with have only negative elements
    direction_count = sum([1 for val in difference if val < 0])
    # direction count 0 is all descending array and the other is increasing array
    # also weed out entries where 0 is present in difference (two equal values in levels)
    if (direction_count == 0 or direction_count == len(difference)) and 0 not in difference:
        # check whether the difference is between 1 <= difference <= 3
        if max(abs(min(difference)), max(difference)) < 4:
            safe_count_1 += 1
            safe_count_2 += 1
            is_safe = True
    # only check unsafe reports, whether it can be made safe with omission
    if not is_safe:
        # create sub-arrays by removing one element at a time
        for idx in range(len(report)):
            levels = report[0:idx] + report[idx+1:]
            difference = [levels[i - 1] - levels[i] for i in range(1, len(levels))]
            direction_count = sum([1 for val in difference if val < 0])
            # if even one safe report is found, it is proof enough that report can be made safe by omission
            # so no need to continue further
            if (direction_count == 0 or direction_count == len(difference)) and 0 not in difference:
                if max(abs(min(difference)), max(difference)) < 4:
                    safe_count_2 += 1
                    break

print("Part 1. Safe Reports = ", safe_count_1)
print("Part 2. Safe Reports (Reworked) = ", safe_count_2)