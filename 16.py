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

# part_1 = 0
# for ticket_value in ticket:
#         part_1 += invalid_value(rules, ticket_value)

# print(part_1)
