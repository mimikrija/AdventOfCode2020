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


def get_destination_label(destination_cup, not_allowed):
    while True:
        if destination_cup < min_label:
            destination_cup = max_label
        if destination_cup not in not_allowed:
            break
        destination_cup -= 1

    return destination_cup

def print_cups(in_cups, head_cup):
    current_cup = head_cup
    printed = ''
    for _ in range(circle_size-1):
        printed += ''+ str(cups_circle[current_cup])
        current_cup = cups_circle[current_cup]
    return (printed)

def get_crabby(cups_circle):
    first_picked, last_picked, picked_up = get_picked_up(current_cup, cups_circle)
    destination = get_destination_label(current_cup-1, picked_up)
    # shift the cups:
    cups_circle[current_cup] = cups_circle[last_picked]
    cups_circle[last_picked] = cups_circle[destination]
    cups_circle[destination] = first_picked


# Party 1

input_cups = '467528193'
circle_size = len(input_cups)

# linked dictionary
cups_circle = {}
for n, cup in enumerate(input_cups):
    cups_circle[int(cup)] = int(input_cups[(n+1)%circle_size])



min_label = min(cups_circle.keys())
max_label = max(cups_circle.keys())

current_cup = list(cups_circle.keys())[0]


for move in range(100):
    get_crabby(cups_circle)
    current_cup = cups_circle[current_cup]


print(f'Labels on the cups after {move+1} moves of the crabby cups, starting after cup labeled "1", are: {print_cups(cups_circle, 1)}')
# Labels on the cups after 100 moves of the crabby cups, starting after cup labeled "1", are: 43769582

#quit()
# party 2


# assemble the big circle
first_label = int(input_cups[0])
next_label = max(int(num) for num in input_cups) + 1

cups_big_circle = {}
for n, cup in enumerate(input_cups):
    if n < len(input_cups)-1:
        cups_big_circle[int(cup)] = int(input_cups[(n+1)])
    else:
        cups_big_circle[int(cup)] = next_label

for n in range(next_label, 1000000):
    cups_big_circle[n] = n + 1

cups_big_circle[1000000] = first_label
# big circle assembled

circle_size = len(cups_big_circle)
min_label = min(cups_big_circle.keys())
max_label = max(cups_big_circle.keys())

current_cup = first_label
for move in range(10000000):
    get_crabby(cups_big_circle)
    current_cup = cups_big_circle[current_cup]



first_star_is_under = cups_big_circle[1]
second_star_is_under = cups_big_circle[first_star_is_under]
party_2 = first_star_is_under*second_star_is_under

print(f'Labels on the cups after {move+1} moves of the MEGA crabby cups, starting after cup labeled "1", are: {first_star_is_under}, {second_star_is_under}!')
print(f'Party 2 solution is: {party_2}!')
# Labels on the cups after 10000000 moves of the MEGA crabby cups, starting after cup labeled "1", are: 489710, 540509!
# Party 2 solution is: 264692662390!
