input_cups = '389125467'
CIRCLE_SIZE = len(input_cups)

# linked dictionary
cups_circle = {}
for n, cup in enumerate(input_cups):
    cups_circle[int(cup)] = int(input_cups[(n+1)%CIRCLE_SIZE])

def get_picked_up(in_current_cup, in_cups):
    picked_up = {}
    current_cup = in_cups[in_current_cup]
    for _ in range(3):
        next_cup = in_cups[current_cup]
        picked_up[current_cup] = next_cup
        current_cup = next_cup
    return(picked_up)


def get_destination_label(current_cup, picked_up, in_cups):
    destination_cup = current_cup - 1
    where_to_look = set(in_cups.keys()).difference(set(picked_up.keys()))
    if destination_cup == 0:
        destination_cup = max(where_to_look)
    if destination_cup in where_to_look:
        return destination_cup
    else:
        return get_destination_label(destination_cup, picked_up, cups)
