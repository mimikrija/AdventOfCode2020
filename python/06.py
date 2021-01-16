# Day 6: Custom Customs

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
    for count_letters in count_answers.values():
        part_2 += count_letters == people_in_group

print(f'The sum of all questions answered is: {part_1}!')
# The sum of all questions answered is: 6778!

print(f'The sum of questions answered by everyone in the group is: {part_2}!')
# The sum of questions answered by everyone in the group is: 3406!
