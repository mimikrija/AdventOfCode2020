import collections
# read & parse input
# 1. read data in bulks split by \n\n
customs_input = open('inputs/06').read().split('\n\n')

part_1 = 0
part_2 = 0
for answers in customs_input:
    count = collections.Counter(answers)
    people_in_group = count['\n']+1
    for letter, num in count.items():
        if letter != '\n':
            part_1 += 1
        if num == people_in_group:
            part_2 += 1

print(part_1)
# 6778

print(part_2)
# 3406
