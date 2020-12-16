import re

def invalid_value(rules, ticket_field):
    """if present, returns invalid ticket field"""
    is_invalid = True
    for rule in rules:
        l_1, u_1, l_2, u_2 = rule
        is_invalid &= ticket_field not in range(l_1, u_1 + 1) and ticket_field not in range(l_2, u_2 + 1)
    if is_invalid:
        return ticket_field
    else:
        return 0

re_digits = re.compile(r'\d+')
re_words = re.compile(r'[a-z]+\s*[a-z]*')

# parse input
# read & parse input
# read data in bulks split by \n\n
tickets_input = open('inputs/16').read().split('\n\n')
# get rules (first block) into a dictionary category: ranges
rules_input = tickets_input[0].split('\n')
rules = {re.findall(re_words,rule)[0]: re.findall(re_digits, rule) for rule in rules_input}
for category, ranges in rules.items():
    rules[category] = [int(num) for num in ranges]

# read and parse my ticket (second block)
my_ticket = re.findall(re_digits, tickets_input[1])
my_ticket = [int(num) for num in my_ticket]

# read and parse all other tickets (third block)
other_tickets_input = tickets_input[2].split('\n')[1:]
other_tickets_input = [re.findall(re_digits,ticket) for ticket in other_tickets_input]
other_tickets = [[int(num) for num in ticket] for ticket in other_tickets_input]


part_1 = sum([invalid_value(rules.values(),ticket_value) for ticket in other_tickets for ticket_value in ticket]) # 26009
print(f'The sum of all invalid values is {part_1}!')

# discard invalid tickets:
valid_tickets = [ticket for ticket in other_tickets
                if sum([invalid_value(rules.values(), ticket_value) for ticket_value in ticket]) == 0]
