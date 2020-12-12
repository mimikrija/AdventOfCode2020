import copy

def neighbours(input_configuration, position):
    """ returns a list of coordinates of all immediate neighbors of `position` in `input_configuration`"""

    row_pos, seat_pos = position
    return [(check_row, check_seat)
        for check_row in range (row_pos-1, row_pos + 2) for check_seat in range (seat_pos-1, seat_pos+2)
        if (check_row != row_pos or check_seat != seat_pos)
        and (check_row, check_seat) in input_configuration.keys()]

def is_seat_desirable(input_configuration, position):
    """ checks whether a seat in `position` in `input_configuration` is desirable
     given the rules from part 1: all neighbouring seats must be empty """

    # seat is not even available, return
    if input_configuration[position] != 'L':
        return False
    count = 0
    checked_seats = 0
    for check_position in neighbours(input_configuration, position):
        checked_seats += 1
        count += input_configuration[check_position] == 'L'
    return checked_seats == count

def is_seat_undesirable(input_configuration, position):
    """ checks whether a seat in `position` in `input_configuration` is no longer
    desirable given the rules from part 1: at least 4 neighbouring seats must be occupied """

    # seat is not even occupied, return
    if input_configuration[position] != '#':
        return False
    count = 0
    for check_position in neighbours(input_configuration, position):
        count += input_configuration[check_position] == '#'
    if count >= 4:
        return True
    return False

def update_configuration(input_configuration):
    """ updates `input_configuration` following rules from part 1
    and returns new configuration as `output_configuration` """

    output_configuration = input_configuration.copy()
    for position, occupancy in input_configuration.items():
        # take seat if desireable
        if is_seat_desirable(input_configuration, position):
            output_configuration[position] = '#'
        # leave seat if undesirable
        if is_seat_undesirable(input_configuration, position):
            output_configuration[position] = 'L'
    return output_configuration

def visible_seats(input_configuration, position):
    """ returns a list of all seats coordinates visible from `position` in `input_configuration` """

    visible = []
    INCREMENTS = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
        'u-l': (-1, -1),
        'u-r': (-1, 1),
        'd-l': (1, -1),
        'd-r': (1, 1)
    }

    for (dx, dy) in INCREMENTS.values():
        check_row, check_seat = position
        while check_row in range (0, total_rows) and check_seat in range (0, total_seats):
            check_row += dx
            check_seat += dy
            if (check_row, check_seat) in input_configuration.keys():
                visible.append((check_row, check_seat))
                break
    return visible

def is_seat_desirable_new_rule(input_configuration, position):
    """ checks whether a seat in `position` in `input_configuration` is desirable
     given the rules from part 2: all seats visible from it must be empty """

    # seat is not even available, return
    if input_configuration[position] != 'L':
        return False
    count = 0
    checked_seats = 0
    for check_position in visible_seats(input_configuration, position):
        checked_seats += 1
        count += input_configuration[check_position] == 'L'
    return checked_seats == count

def is_seat_undesirable_new_rule(input_configuration, position):
    """ checks whether a seat in `position` in `input_configuration` is no longer
    desirable given the rules from part 2: at least 5 seats visible from it must be occupied """

    # seat is not even occupied, return
    if input_configuration[position] != '#':
        return False
    count = 0
    for check_position in visible_seats(input_configuration, position):
        count += input_configuration[check_position] == '#'
    if count >= 5:
        return True
    return False

def update_configuration_new_rule(input_configuration):
    """ updates `input_configuration` following rules from part 2
    and returns new configuration as `output_configuration` """
    output_configuration = input_configuration.copy()
    for position, occupancy in input_configuration.items():
        # take seat if desireable
        if is_seat_desirable_new_rule(input_configuration, position):
            output_configuration[position] = '#'
        # leave seat if undesirable
        if is_seat_undesirable_new_rule(input_configuration, position):
            output_configuration[position] = 'L'
    return output_configuration

# parse input
with open('inputs/11-ex') as inputfile:
    rows = inputfile.readlines()

seat_configuration = []
for row in rows:
    row = row.strip()
    row = [c for c in row]
    seat_configuration.append(row)

# get input dimensions
total_rows = len(seat_configuration)
total_seats = len(row)

all_coordinates = {}
for row_c, row in enumerate(seat_configuration):
    for seat_c, seat in enumerate(row):
        if seat != '.':
            all_coordinates[(row_c,seat_c)] = seat


current_configuration = all_coordinates.copy()
#output_configuration = {}

while True:
    next_configuration = update_configuration(current_configuration)
    if next_configuration == current_configuration:
        break
    else:
        current_configuration = next_configuration.copy()

part_1 = 0
for occupancy in current_configuration.values():
    part_1 += occupancy == '#'

print(f'The number of occupied seats is: {part_1}!')
# The number of occupied seats is: 2204!

current_configuration = all_coordinates.copy()
#output_configuration = {}

while True:
    next_configuration = update_configuration_new_rule(current_configuration)
    if next_configuration == current_configuration:
        break
    else:
        current_configuration = next_configuration.copy()

part_2 = 0
for occupancy in current_configuration.values():
    part_2 += occupancy == '#'

print(f'The number of occupied seats following new rules is: {part_2}!')
# The number of occupied seats following new rules is: 1986!
