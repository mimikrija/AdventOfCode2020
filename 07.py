import re

with open('inputs/07-ex') as inputfile:
    inputs = inputfile.readlines()

everything = [line.strip() for line in inputs]

def find_outter_bags(find_next, all_solutions):
    while find_next != []:
        for bag in find_next:
            find_next = [rule.split(' bags contain')[0] for rule in everything if bag in rule and rule.find(bag) != 0]
            find_outter_bags(find_next,all_solutions)
            all_solutions += find_next
    return len(set(all_solutions))

part_1 = find_outter_bags(['shiny gold'],[])

print(f'{part_1} bag colors contain at least one shiny gold bag!')
# 246 bag colors contain at least one shiny gold bag!

def count_bags(quantities, children_quantities):
    quantities = [int(num) for num in quantities]
    children_quantities = [int(num) for num in children_quantities]
    count = sum(quantities)
    for multi, qt in zip(quantities, children_quantities):
        count += multi*qt
    return count
# parse input into dictionary
re_digits = re.compile(r'\d')
re_two_words = re.compile(r'[a-z]+ [a-z]+')

bags_dict = {}
for rule in everything:
    bag, children = rule.split(' bags contain')
    quantities = re.findall(re_digits,children)
    quantities = [int(qt) for qt in quantities]
    children = re.findall(re_two_words,children)
    children = [children, quantities]
    bags_dict[bag] = children

