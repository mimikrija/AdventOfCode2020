from collections import Counter
with open('inputs/10') as inputfile:
    inputs = inputfile.readlines()

inputs = [int(line.strip()) for line in inputs]

inputs.sort()

diffs = [j-i for i,j in zip(inputs[:-1],inputs[1:])]

counted_diffs = Counter(diffs)

print((counted_diffs[1]+1)*(counted_diffs[3]+1))
