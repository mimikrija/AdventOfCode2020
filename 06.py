from collections import Counter

# read data in bulks split by \n\n :)
customs_input = open('inputs/06').read().split('\n\n')

part_1 = 0
part_2 = 0
for answers in customs_input:
    count_answers = Counter(answers)
    # part 1: count all letters that appear in one bulk
    part_1 += len(count_answers) - ('\n' in count_answers.keys())
    # part 2: count only letters that appear in *every* line of bulk
    people_in_group = count_answers['\n'] + 1
    for _, num in count_answers.items():
        part_2 += num == people_in_group

print(part_1)
# 6778

print(part_2)
# 3406
