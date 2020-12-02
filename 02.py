import re

def is_password1(input):
    min_count = int(input[0])
    max_count = int(input[1])
    character = input[2]
    password = input[3]
    return password.count(character) >= min_count and password.count(character) <= max_count

def is_password2(input):
    # do the min max stuff in a separate function
    min_count = int(input[0])
    max_count = int(input[1])
    character = input[2]
    password = input[3]
    return ( password[min_count-1] == character and password[max_count-1] != character) or ( password[min_count-1] != character and password[max_count-1] == character)


with open('inputs/02') as inputfile:
    inputs = inputfile.readlines()

words =re.compile(r'\w+')

rules = []
for line in inputs:
    rules.append(re.findall(words,line))

solution1 = 0
for rule in rules:
    solution1 += is_password1(rule)

solution2 = 0
for rule in rules:
    solution2 += is_password2(rule)

print(f'The number of valid passwords is {solution1}!')
print(f'The number of valid passwords is {solution2}, following the second rule!')
# The number of valid passwords is 536!
# The number of valid passwords is 558, following the second rule!
