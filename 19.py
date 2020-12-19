# just try it for example 1
# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"
applied_rules = {4: ["a"], 5: ["b"]} # I think I can use eval to do this directly on input if "letter in input"/"numbers not present in input"/"only one space present in input"
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
