import sys
sys.setrecursionlimit(10**6)

with open("example") as file:
    content = file.readlines()

def calculate_secret_number(number, step):
    if step == 0:
        return number
    else:
        mul_result = number * 64
        number = number ^ mul_result
        number = number % 16777216
        div_result = number // 32
        number = number ^ div_result
        number = number % 16777216
        mul_result = number * 2048
        number = number ^ mul_result
        number = number % 16777216
        return calculate_secret_number(number, step - 1)

numbers = []
for line in content:
    numbers.append(int(line.strip()))

total = 0
for num in numbers:
    total += calculate_secret_number(num, 2000)
print(total)



