import re

def invalid_value(rules, ticket_field):
    """if present, returns invalid ticket field"""
    is_invalid = True
    for rule in rules:
        is_invalid &= ticket_field not in rule
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
rules = {re.findall(re_words,rule)[0]: (int(num) for num in re.findall(re_digits, rule)) for rule in rules_input}
for category, ranges in rules.items():
    low, mid_l, mid_h, high = ranges
    rule_range = set(range(low, high+1)).difference(range(mid_l+1, mid_h))
    rules[category] = rule_range

# read and parse my ticket (second block)
my_ticket = re.findall(re_digits, tickets_input[1])
my_ticket = [int(num) for num in my_ticket]

# read and parse all other tickets (third block)
other_tickets_input = tickets_input[2].split('\n')[1:]
other_tickets_input = [re.findall(re_digits,ticket) for ticket in other_tickets_input]
other_tickets = [[int(num) for num in ticket] for ticket in other_tickets_input]


part_1 = sum([invalid_value(rules.values(),ticket_value) for ticket in other_tickets for ticket_value in ticket])
print(f'The sum of all invalid values is {part_1}!')
# The sum of all invalid values is 26009!


# discard invalid tickets:
valid_tickets = [ticket for ticket in other_tickets
                if sum([invalid_value(rules.values(), ticket_value) for ticket_value in ticket]) == 0]

# generate lists which contain all first, all second, etc. fields of all tickets
num_of_fields = len(rules)
all_values_per_field = {n: [ticket[n] for ticket in valid_tickets] for n in range(0, num_of_fields)}

# dictionary of all possible matches, field: all_matched_categories
possible_matches = {field: [] for field in all_values_per_field.keys()}
for category, rule in rules.items():
    for field, field_values in all_values_per_field.items():
        if sum([invalid_value([rule], field_value) for field_value in field_values]) == 0:
            possible_matches[field].append(category)


def match_fields(in_possible):
    """ removes unique match from `in_possible` and returns `matched_category` and `field`"""
    for field, possible_categories in in_possible.items():
        if len(possible_categories) == 1:
            matched_category = in_possible.pop(field)[0]
            for name, cat_list in in_possible.items():
                #new_cat_list = cat_list
                cat_list.remove(possible_categories[0])
                in_possible[name] = cat_list
            return matched_category, field

# do find_unique until we match all the fields
final_match = {}
while True:
    category, field = match_fields(possible_matches)
    final_match[category] = field
    if len(final_match) == len(rules):
        break

part_2 = 1
for category, position in final_match.items():
    if 'departure' in category:
        part_2 *= my_ticket[position]

print(f'The sum of product of all ticket fields containing the word "departure" is {part_2}!')
# The sum of product of all ticket fields containing the word "departure" is 589685618167!
