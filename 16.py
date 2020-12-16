def is_value_valid(rule, ticket_field):
    l_1, u_1, l_2, u_2 = rule
    return ticket_field in range(l_1, u_1 + 1) or ticket_field in range(l_2, u_2 + 1)

