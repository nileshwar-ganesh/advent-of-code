with open("data") as file:
    content = file.readlines()

reports = []
for entry in content:
    reports.append([int(val) for val in entry.strip().split()])

safe_count_1 = 0
safe_count_2 = 0
for report in reports:
    is_safe = False
    difference = [report[i-1] - report[i] for i in range(1, len(report))]
    direction_count = sum([1 for val in difference if val < 0])
    if (direction_count == 0 or direction_count == len(difference)) and 0 not in difference:
        if max(abs(min(difference)), max(difference)) < 4:
            safe_count_1 += 1
            safe_count_2 += 1
            is_safe = True

    if not is_safe:
        for idx in range(len(report)):
            levels = report[0:idx] + report[idx+1:]
            difference = [levels[i - 1] - levels[i] for i in range(1, len(levels))]
            direction_count = sum([1 for val in difference if val < 0])
            if (direction_count == 0 or direction_count == len(difference)) and 0 not in difference:
                if max(abs(min(difference)), max(difference)) < 4:
                    safe_count_2 += 1
                    break

print("Part 1. Safe Reports = ", safe_count_1)
print("Part 2. Safe Reports (Reworked) = ", safe_count_2)