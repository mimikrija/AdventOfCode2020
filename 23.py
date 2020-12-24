input_cups = '467528193'
circle_size = len(input_cups)

# linked dictionary
cups_circle = {}
for n, cup in enumerate(input_cups):
    cups_circle[int(cup)] = int(input_cups[(n+1)%circle_size])

def get_picked_up(in_current_cup, in_cups):
    picked_up = set()
    current_cup = in_cups[in_current_cup]
    first_picked_up = current_cup
    for _ in range(3):
        picked_up.add(current_cup)
        next_cup = in_cups[current_cup]
        last_picked_up = current_cup
        current_cup = next_cup
    return first_picked_up, last_picked_up, picked_up


def get_destination_label(current_cup, picked_up, in_cups):
    destination_cup = current_cup - 1
    where_to_look = set(in_cups.keys()).difference(picked_up)
    if destination_cup == 0:
        destination_cup = max(where_to_look)
    if destination_cup in where_to_look:
        return destination_cup
    else:
        return get_destination_label(destination_cup, picked_up, in_cups)

def print_cups(in_cups, head_cup):
    current_cup = head_cup
    printed = ''
    for _ in range(circle_size-1):
        printed += ''+ str(cups_circle[current_cup])
        current_cup = cups_circle[current_cup]
    return (printed)


current_cup = list(cups_circle.keys())[0]

def get_crabby(cups_circle):
    first_picked, last_picked, picked_up = get_picked_up(current_cup, cups_circle)
    destination = get_destination_label(current_cup, picked_up, cups_circle)

    cups_circle[current_cup] = cups_circle[last_picked]
    cups_circle[last_picked] = cups_circle[destination]
    cups_circle[destination] = first_picked

for move in range(100):
    get_crabby(cups_circle)
    current_cup = cups_circle[current_cup]


print(f'Labels on the cups after {move+1} moves of the crabby cups, starting after cup labeled "1", are: {print_cups(cups_circle, 1)}')
# Labels on the cups after 100 moves of the crabby cups, starting after cup labeled "1", are: 43769582
