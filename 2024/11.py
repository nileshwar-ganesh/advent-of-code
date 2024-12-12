def split_stone(stones):
    global counter, final_stones
    st = []
    for val in stones:
        if val == 0:
            st.append(1)
        elif len(str(val)) % 2 == 0:
            st.append(int(str(val)[:len(str(val)) // 2]))
            st.append(int(str(val)[len(str(val)) // 2:]))
        else:
            st.append(val * 2024)
    counter += 1
    if counter == 25:
        final_stones = st
        return True
    else:
        split_stone(st)

# read from data file
with open("data") as file:
    content = file.readlines()

counter = 0
final_stones = []
for line in content:
    stones = [int(val) for val in line.strip().split()]

split_stone(stones)
print(len(final_stones))

