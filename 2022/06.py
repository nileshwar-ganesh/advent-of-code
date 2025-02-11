import sys

sys.setrecursionlimit(10**6)

def find_marker(data, marker_length):
    clip = data[:marker_length]
    if len(clip) == len(set(clip)):
        return marker_length
    else:
        return 1 + find_marker(data[1:], marker_length)


with open("example") as file:
    content = file.readlines()

datastream = content[0]
print("Part 1. Characters need to be processed before the first start-of-packet marker = ", find_marker(datastream, 4))
print("Part 2. Characters need to be processed before the first start-of-message marker = ", find_marker(datastream, 14))


