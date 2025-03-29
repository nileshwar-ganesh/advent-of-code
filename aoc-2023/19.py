import re
with open("example") as file:
    content = file.readlines()

workflows = []
ratings = {}
is_ratings = False
variables = ["x", "m", "a", "s"]
entry = 1
for line in content:
    if line == "\n":
        is_ratings = True
        continue
    if is_ratings:
        values = [int(value) for value in re.findall(r"\d+", line.strip())]

    for index, value in enumerate(values):
        pass
