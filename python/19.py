# Day 19: Monster Messages

import re

rules_and_messages = open('inputs/19').read().split('\n\n')
rules, messages = rules_and_messages
rules = rules.split('\n')
messages = messages.split('\n')

# parse applied rules:
applied_rules = {}
for rule in rules:
    if '\"' in rule:
        split_pos = rule.index(':')
        rule_no = int(rule[:split_pos])
        rule_value = [eval(rule[split_pos+1:])]
        applied_rules[rule_no] = rule_value

re_numbers = re.compile(r'\d+')
not_applied_rules = {}
# parse first type of not applied rules:
for rule in rules:
    if '\"' not in rule and "|" not in rule:
        split_pos = rule.index(':')
        rule_no = int(rule[:split_pos])
        rule_value = re.findall(re_numbers, rule[split_pos+1:])
        rule_value = [tuple(int(num) for num in rule_value)]
        not_applied_rules[rule_no] = rule_value

# parse second type of not applied rules:
for rule in rules:
    if "|" in rule:
        split_pos = rule.index(':')
        rule_no = int(rule[:split_pos])
        rest = rule[split_pos+1:]
        split_pos_2 = rest.index('|')
        rule_value = []
        for rule_tuple in rest.split('|'):
            rule_value += [tuple(int(num) for num in re.findall(re_numbers, rule_tuple))]
        not_applied_rules[rule_no] = rule_value


def who_can_I_apply_next(applied_rules, not_applied_rules):
    rules_to_be_applied_next = []
    for rule_no, rule in not_applied_rules.items():
        to_be_applied = set(n for tup in rule for n in tup)
        if all(rule in applied_rules.keys() for rule in to_be_applied):
            rules_to_be_applied_next.append(rule_no)
    return rules_to_be_applied_next

def apply_rule(applied_rules, not_applied_rules, rule_no):
    rule_tuples = not_applied_rules[rule_no]
    result = set()
    for rule_tuple in rule_tuples:
        if len(rule_tuple) == 1:
            first = rule_tuple[0]
            test = {one for one in applied_rules[first]}
        if len(rule_tuple) == 2:
            first, second = rule_tuple
            test = {one + two for one in applied_rules[first] for two in applied_rules[second]}
        if len(rule_tuple) == 3:
            first, second, third = rule_tuple
            test = {one + two + three for one in applied_rules[first] for two in applied_rules[second] for three in applied_rules[third]}
        result = result.union(test)
    return set(result)

while not_applied_rules:
    next_rules = who_can_I_apply_next(applied_rules, not_applied_rules)
    for next_rule in next_rules:
        applied_rules[next_rule] = apply_rule(applied_rules, not_applied_rules, next_rule)
        del not_applied_rules[next_rule]

matches = applied_rules[0]

part_1 = 0

for message in messages:
    part_1 += message in matches

print(f'The number of messages that match is {part_1}!')
# The number of messages that match is 109!

# part 2:
# if we apply the loop(s) and rules, rules [8] and [11] call them selves, which means that
# rule [8] becomes:
# [42] | [42][8]
# [42] | [42][42][8]
# [42] | [42][42][42][8]
# ... you get the picture

# rule [11] becomes:
# [42][31] | [42][11][31]
# [41][31] | [42][42][11][31][31]
# [41][31] | [42][42][42][11][31][31][31]
# ... etc

# so rule [0] = [8][11] looks something like this:
# n*[42]m*[31], n > m (because [42] appears more times even in the zero iteration)

# so let's filter messages based on this rule


lenghts_42 = set(len(rule) for rule in applied_rules[42])
len_42 = lenghts_42.pop()
lengths_31 = set(len(rule) for rule in applied_rules[31])
len_31 = lengths_31.pop()
if len_31 == len_42:
    len_block = len_31
else:
    print("You will need to write a better program to solve this")
    quit()

# first, choose only messages that match the specific size:
subset_by_length = set()
for message in messages:
    if len(message) % len_block == 0:
        subset_by_length.add(message)

# which doesn't really help much because all the messages satisfy that rule
# but I didn't know that (at least for the input data) - good to check anyway

matches_part_2 = set()
for message in messages:

    # check for consecutive [42] blocks in the message and count how many times they appear
    count_42 = 0
    while len_block*(count_42 + 1) <= len(message):
        block = message[len_block*count_42:len_block*(count_42 + 1)]
        if block in applied_rules[42]:
            count_42 += 1
        else:
            break
    # check if next consecutive block is [31], if not - we're not interested
    if block not in applied_rules[31]:
        continue

    # now check for consecutive [31] blocks
    count_31 = 0
    while len_block*(count_42 + count_31 + 1) <= len(message):
        block = message[len_block*(count_42+count_31):len_block*(count_42 + count_31 + 1)]
        if block in applied_rules[31]:
            count_31 += 1
        else:
            break
        if count_31 >= count_42:
            break
    if (count_31 + count_42) == len(message)/len_block and count_42 > count_31:
        matches_part_2.add(message)

part_2 = len(matches_part_2)
print(f'The number of messages that match with continuous loops is {part_2}!')
# The number of messages that match with continuous loops is 301!
