# just try it for example 1
# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"
applied_rules = {3: "b", 1: "a"} # I think I can use eval to do this directly on input if "letter in input"/"numbers not present in input"/"only one space present in input"
not_applied_rules = {0: [(1,2)], 2: [(1,3),(3,1)]}

def who_can_I_apply_next(applied_rules, not_applied_rules):
    for rule_no, rule in not_applied_rules.items():
        to_be_applied = set(n for tup in rule for n in tup)
        if all(rule in applied_rules.keys() for rule in to_be_applied):
            return rule_no

print(who_can_I_apply_next(applied_rules,not_applied_rules))
