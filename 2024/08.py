with open("data") as file:
    content = file.readlines()

# creating a readable matrix out of input data
matrix = []
for line in content:
    line = [char for char in line.strip()]
    matrix.append(line)

# dictionary to store frequency and its node locations
frequencies = {}
node_locations = []
for row, line in enumerate(matrix):
    for col, value in enumerate(line):
        if value != ".":
            if value not in frequencies.keys():
                frequencies[value] = [(row, col)]
            else:
                frequencies[value].append((row, col))
            # marker to save node locations
            if (row, col) not in node_locations:
                node_locations.append((row, col))

# Part 1. if an anti-node appears on the frequency node, ignore it
anti_node_count = 0
for key in frequencies.keys():
    for idx, node in enumerate(frequencies[key]):
        for n in frequencies[key][idx+1:]:
            r_diff = n[0] - node[0]
            c_diff = n[1] - node[1]
            if 0 <= node[0] - r_diff < len(matrix) and 0 <= node[1] - c_diff < len(matrix[0]):
                # making sure that overlapping anti-nodes are not considered
                if (node[0] - r_diff, node[1] - c_diff) not in node_locations:
                    anti_node_count += 1
            if 0 <= n[0] + r_diff < len(matrix) and 0 <= n[1] + c_diff < len(matrix[0]):
                # making sure that overlapping anti-nodes are not considered
                if (n[0] + r_diff, n[1] + c_diff) not in node_locations:
                    anti_node_count += 1
print("Part 1. Anti-node count (ignoring ones appearing on frequency node) = ", anti_node_count)

# Part 2. anti nodes not appear just once, but appear in an equidistant line
# also, anti-nodes overlapping with frequency nodes are considered
# overlapping anti-nodes are considered just once
anti_node_count = 0
anti_node_loc = []
for key in frequencies.keys():
    for idx, node in enumerate(frequencies[key]):
        for n in frequencies[key][idx+1:]:
            r_diff = n[0] - node[0]
            c_diff = n[1] - node[1]
            n1 = node[0]
            c1 = node[1]
            # instead of a simple if condition, we have to consider locations in a loop
            while 0 <= n1 - r_diff < len(matrix) and 0 <= c1 - c_diff < len(matrix[0]):
                # only consider one anti-node at a location, if more than one
                if (n1 - r_diff, c1 - c_diff) not in anti_node_loc:
                    anti_node_loc.append((n1 - r_diff, c1 - c_diff))
                anti_node_count += 1
                n1 -= r_diff
                c1 -= c_diff
            n1 = n[0]
            c1 = n[1]
            while 0 <= n1 + r_diff < len(matrix) and 0 <= c1 + c_diff < len(matrix[0]):
                # only consider one anti-node at a location, if more than one
                if (n1 + r_diff, c1 + c_diff) not in anti_node_loc:
                    anti_node_loc.append((n1 + r_diff, c1 + c_diff))
                anti_node_count += 1
                n1 += r_diff
                c1 += c_diff
# finally, add nodes which have not been added to anti-node location yet
for node in node_locations:
    if node not in anti_node_loc:
        anti_node_loc.append(node)
print("Part 2. Anti-node count (considering anti-nodes created in a line) = ", len(anti_node_loc))
