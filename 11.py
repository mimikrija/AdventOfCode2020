import copy
import collections

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

def count_occupied_seats(input_configuration):
    counter = collections.Counter(input_configuration.values())
    return counter['#']


with open('inputs/11') as inputfile:
    inputs = inputfile.readlines()

# get input dimensions
total_rows, total_seats = len(inputs), len(inputs[0].strip())

# parse input into a dictionary seat coordinates: seat ocupancy
initial_configuration = {(row_num, seat_num): seat
                        for row_num, row in enumerate(inputs)
                        for seat_num, seat in enumerate(row.strip())
                        if seat!='.'}

def solve_day_11(puzzle_part, initial_configuration):
    # set initial conditions
    current_configuration = initial_configuration.copy()

    # keep updating configurations until two consecutive configurations match
    while True:
        if puzzle_part == 'part 1':
            next_configuration = update_configuration(current_configuration)
        if puzzle_part == 'part 2':
            next_configuration = update_configuration_new_rule(current_configuration)
        if next_configuration == current_configuration:
            break
        else:
            current_configuration = next_configuration.copy()

    print(f'The number of occupied seats in {puzzle_part} is: {count_occupied_seats(current_configuration)}!')


solve_day_11('part 1', initial_configuration)
solve_day_11('part 2', initial_configuration)
# The number of occupied seats in part 1 is: 2204!
# The number of occupied seats in part 2 is: 1986!
