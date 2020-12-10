from collections import Counter
with open('inputs/10') as inputfile:
    inputs = inputfile.readlines()

inputs = [int(line.strip()) for line in inputs]

inputs.sort()
inputs = [0] + inputs + [max(inputs) + 3]

diffs = [j-i for i,j in zip(inputs[:-1],inputs[1:])]

counted_diffs = Counter(diffs)

print((counted_diffs[1])*(counted_diffs[3]))

test_list = [3] + diffs
counted_ones = []
for i in range(1,4):
    sublist = [3] + (i+1)*[1] + [3]
    count_sublist = len([sublist for idx in range(len(test_list)) if test_list[idx : idx + len(sublist)] == sublist])
    counted_ones.append((i, count_sublist))

combinations = {
    1: 2,
    2: 4,
    3: 7
}

part_2 = 1
for n, c in counted_ones:
    part_2 *= combinations[n]**c

print(part_2) # 226775649501184
