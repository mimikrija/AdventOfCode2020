import collections
# read & parse input
# 1. read data in bulks split by \n\n
customs_input = open('inputs/06').read().split('\n\n')
print(customs_input)
part_1 = 0
for answers in customs_input:
    count = collections.Counter(answers)
    for letter, num in count.items():
        if letter != '\n':
            part_1 += 1

print(part_1)
