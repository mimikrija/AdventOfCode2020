rules_and_messages = open('inputs/19-ex').read().split('\n\n')
rules, messages = rules_and_messages
rules = rules.split('\n')
messages = messages.split('\n')

# separate applied rules:
applied_rules = {}
for rule in rules:
    if '\"' in rule:
        split_pos = rule.index(':')
        rule_no = int(rule[:split_pos])
        rule_value = [eval(rule[split_pos+1:])]
        applied_rules[rule_no] = rule_value



not_applied_rules = {0: [(4, 1, 5)], 1: [(2,3),(3,2)], 2: [(4,4), (5, 5)], 3: [(4, 5), (5, 4)]}

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
print(matches)



# test if the example works
if all(test in matches for test in ['aaaabb', 'aaabab', 'abbabb', 'abbbab', 'aabaab', 'aabbbb', 'abaaab', 'ababbb']):
    print('succes!')
