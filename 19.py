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

# these are the valid match combinations:
# 42    42    31
# 42    42 11 31
# 42  8 42    31
# 42  8 42 11 31

# which is basically all matches which: begin with 42 and end with 31 // this is the first pass
# it helps that the matches for 42 and 31 are all of same len!

lenghts_42 = set()
for rule in applied_rules[42]:
    lenghts_42.add(len(rule))
len_42 = lenghts_42.pop()

lengths_31 = set()
for rule in applied_rules[31]:
    lengths_31.add(len(rule))
len_31 = lengths_31.pop()
# ok so let's go
# first subset of matches are all messages which BOTH begin with 42 and end with 31:
first_subset = set()
for message in messages:
    for rule_1 in applied_rules[42]:
        if message[:len_42] == rule_1:
            for rule_2 in applied_rules[31]:
                if message[-len_31:] == rule_2:
                    first_subset.add(message)

# now we could solve for the first set, but as we will see later this one is already included in other combos
# 42 42 31


# following three sets are tricky because they contain unknown rules 8 and 11, but we can try and deduce length of rule 11 from the next matches:
# 42 42 ?11? 31 

first_tricky_set = set()
for message in first_subset:
    for rule_1 in applied_rules[42]:
        if message[len_42:2*len_42] == rule_1:
            for rule_2 in applied_rules[31]:
                if message[-len_31:] == rule_2:
                    first_tricky_set.add(message)

lengths_first_tricky_set = set(len(match) for match in first_tricky_set)
lengths_11 = set(match - 2*len_42 - len_31 for match in lengths_first_tricky_set)
# all possible lenghts of set 11


# next we do it for the set with unknown rule 8:
# this check will return all matches for both sets:
# 42 42 31
# 42 ?8? 42 31 (first and last is already satisfied)

second_tricky_set = set()
for message in first_subset:
    for rule_1 in applied_rules[42]:
        if message[-(len_42+len_31):-len_31] == rule_1:
            second_tricky_set.add(message)

lengths_second_tricky_set = set(len(match) for match in second_tricky_set)
lengths_8 = set(match - 2*len_42 - len_31 for match in lengths_second_tricky_set)
# all possible lenghts of set 8

# FINALLY, we check the last set:
# 42 8 42 11 31
# (42) 8 42 11 (31) - first and last rules are already satisfied in the subset we are searching through
# we know the lenghts of all rules
# since rule 11 has only one length, we can do a backward search and just check that:
# total length = len_42 + {len_8} + len_42 + {len_11} + len_31

#if we take into account zero-length 8 and 11 matches, this set actually includes all combinations

last_tricky_set = set()
for message in first_subset:
    for len_11 in lengths_11:
        for len_8 in lengths_8:
            if len(message) == len_42 + len_8 + len_42 + len_11 + len_31:#and len_11 >= len_31+len_42 and len_8 >= len_42:
                for rule in applied_rules[42]:
                    if message[-(len_31+len_11+len_42):-(len_31+len_11)] == rule:
                        last_tricky_set.add(message)

part_2 = len(last_tricky_set)
print(part_2) # 328 not!! # 318 not!! # 87 not

