import copy

def neighbours(input_configuration, position):
    row_pos, seat_pos = position
    return [(check_row, check_seat)
        for check_row in range (row_pos-1, row_pos + 2) for check_seat in range (seat_pos-1, seat_pos+2)
        if (check_row != row_pos or check_seat != seat_pos)
        and (check_row, check_seat) in input_configuration.keys()]

def visible_seats(input_configuration, position):
    visible = []
    row_pos, seat_pos = position
    # up
    for up in range(row_pos - 1, -1, -1):
        check_position = (up, seat_pos)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break

    # left
    for up in range(seat_pos - 1, -1, -1):
        check_position = (row_pos, up)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break

    # down
    for up in range(row_pos + 1, total_rows):
        check_position = (up, seat_pos)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break

    # right
    for up in range(seat_pos + 1, total_seats):
        check_position = (row_pos, up)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break
    
    # up left diagonal
    for x, y in zip( range(row_pos - 1, -1, -1), range(seat_pos - 1, -1, -1)):
        check_position = (x, y)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break

    # up right diagonal
    for x, y in zip( range(row_pos - 1, -1, -1), range(seat_pos + 1, total_seats)):
        check_position = (x, y)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break

    # down left diagonal
    for x, y in zip( range(row_pos + 1, total_rows), range(seat_pos - 1, -1, -1)):
        check_position = (x, y)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break

    # down right diagonal
    for x, y in zip( range(row_pos + 1, total_rows), range(seat_pos + 1, total_seats)):
        check_position = (x, y)
        if check_position in input_configuration.keys():
            visible.append(check_position)
            break

    return visible

def is_seat_desirable(input_configuration, position):
    if input_configuration[position] != 'L':
        return False
    count = 0
    checked_seats = 0
    for check_position in neighbours(input_configuration, position):
        checked_seats += 1
        count += input_configuration[check_position] == 'L'
    return checked_seats == count

def is_seat_undesirable(input_configuration, position):
    if input_configuration[position] != '#':
        return False
    count = 0
    for check_position in neighbours(input_configuration, position):
        count += input_configuration[check_position] == '#'
    if count >= 4:
        return True
    return False

def update_configuration(input_configuration):
    output_configuration = input_configuration.copy()
    for position, occupancy in input_configuration.items():
        # take seat if desireable
        if is_seat_desirable(input_configuration, position):
            output_configuration[position] = '#'
        # leave seat if undesirable
        if is_seat_undesirable(input_configuration, position):
            output_configuration[position] = 'L'
    return output_configuration

# parse input
with open('inputs/11') as inputfile:
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
