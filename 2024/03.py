import re

with open("data") as file:
    content = file.readlines()

expressions = []
for line in content:
    expressions.append(line.strip())

do_list = [] # list of mul functions appearing after do()
dont_list = [] # list of mul functions appearing after don't()
do_status = True # alternating status which keeps track of what to do
for expression in expressions:
    for i in range(len(expression)):
        # checking whether we encounter a do or don't
        if expression[i:i+7] == "don't()":
            do_status = False
        elif expression[i:i+4] == "do()":
            do_status = True
        # and when we encounter a mul
        elif expression[i:i+3] == "mul":
            # first check whether it is valid
            value = expression[i:i+12]
            mul = re.findall(r"mul\(\d{1,3},\d{1,3}\)", value)
            # and then assign it to appropriate list
            if len(mul) > 0:
                if do_status:
                    do_list.append(mul[0])
                else:
                    dont_list.append(mul[0])

# total sum of the do s
sum_do = 0
for entry in do_list:
    val1, val2 = re.findall(r"\d+", entry)
    sum_do += int(val1) * int(val2)
# total sum of the don't s
sum_dont = 0
for entry in dont_list:
    val1, val2 = re.findall(r"\d+", entry)
    sum_dont += int(val1) * int(val2)

print('Part 1. Result of all multiplications = ', sum_do + sum_dont)
print('Part 2. Result of do multiplications = ', sum_do)
