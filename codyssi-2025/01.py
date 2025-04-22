with open("../data-files/d1") as file:
    content = file.readlines()

numbers = []
symbols = None
for line in content:
    if line.strip().isnumeric():
        numbers.append(int(line.strip()))
    symbols = line.strip()

calibration = numbers[0]
for i in range(0, len(symbols)):
    if symbols[i] == '-':
        calibration -= numbers[i + 1]
    else:
        calibration += numbers[i + 1]

calibration = numbers[0]
for i in range(0, len(symbols)):
    if symbols[len(symbols) - i - 1] == '-':
        calibration -= numbers[i + 1]
    else:
        calibration += numbers[i + 1]


calibration = numbers[0] * 10 + numbers[1]
index = len(symbols) - 1
for i in range(2, len(numbers), 2):
    if symbols[index] == '-':
        calibration -= (numbers[i] * 10 + numbers[i + 1])
    else:
        calibration += (numbers[i] * 10 + numbers[i + 1])
    index -= 1

print(calibration)


