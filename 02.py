import re

def is_password(input):
    min_count = int(input[0])
    max_count = int(input[1])
    character = input[2]
    password = input[3]
    return password.count(character) >= min_count and password.count(character) <= max_count

with open('inputs/02') as inputfile:
    inputs = inputfile.readlines()

words =re.compile(r'\w+')

rules = []
for line in inputs:
    rules.append(re.findall(words,line))

solution1 = 0
for rule in rules:
    solution1 += is_password(rule)

print(solution1)
