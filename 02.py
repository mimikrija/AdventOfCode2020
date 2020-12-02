import re

def parse(unparsed_rule):
    first, second, char, word = unparsed_rule
    first, second = int(first), int(second)
    return(first, second, char, word)

def is_password1(input):
    min_count, max_count, character, password = parse(input)
    return max_count >= password.count(character) >= min_count

def is_password2(input):
    first_char, second_char, character, password = parse(input)
    return (password[first_char-1] == character) ^ (password[second_char-1] == character)


with open('inputs/02') as inputfile:
    inputs = inputfile.readlines()

words = re.compile(r'\w+')

part_1 = 0
part_2 = 0

for line in inputs:
    rule = re.findall(words, line)
    part_1 += is_password1(rule)
    part_2 += is_password2(rule)

print(f'The number of valid passwords is {part_1}!')
print(f'The number of valid passwords is {part_2} (following the second rule)!')
# The number of valid passwords is 536!
# The number of valid passwords is 558 (following the second rule)!
