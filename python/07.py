# Day 7: Handy Haversacks

import re

with open('inputs/07') as inputfile:
    inputs = inputfile.readlines()

everything = [line.strip() for line in inputs]

def find_outter_bags(find_next, all_solutions):
    while find_next != []:
        for bag in find_next:
            find_next = [rule.split(' bags contain')[0] for rule in everything if bag in rule and rule.find(bag) != 0]
            find_outter_bags(find_next, all_solutions)
            all_solutions += find_next
    return len(set(all_solutions))

part_1 = find_outter_bags(['shiny gold'], [])

print(f'{part_1} bag colors contain at least one shiny gold bag!')
# 246 bag colors contain at least one shiny gold bag!

def count_bags(one_bag):
    if one_bag == 'no other':
        count = 0
    else:
        multipliers = bags_dict[one_bag][1]
        count = sum(multipliers)
    if 'no other' not in bags_dict[one_bag][0]:
        for child_bag, multiplier in zip(bags_dict[one_bag][0], multipliers):
            count += multiplier*count_bags(child_bag)
    return count

# parse input into dictionary
re_digits = re.compile(r'\d')
re_two_words = re.compile(r'[a-z]+ [a-z]+')

bags_dict = {}
for rule in everything:
    left, right = rule.split(' bags contain')
    quantities = re.findall(re_digits,right)
    quantities = [int(qt) for qt in quantities]
    children = re.findall(re_two_words,right)
    bags_dict[left] = [children, quantities]

part_2 = count_bags('shiny gold')

print(f'Shiny gold bag contains {part_2} bags!')
# Shiny gold bag contains 2976 bags!
