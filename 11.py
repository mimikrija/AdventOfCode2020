import copy

def neighbours(position):
    row_pos, seat_pos = position
    return [(check_row, check_seat)
        for check_row in range (row_pos-1, row_pos + 2) for check_seat in range (seat_pos-1, seat_pos+2)
        if (check_row != row_pos or check_seat != seat_pos)
        and 0 <= check_row < total_rows and 0 <= check_seat < total_seats]

def is_seat_desirable(input_configuration, position):
    count = 0
    checked_seats = 0
    for check_position in neighbours(position):
        if check_position in input_configuration:
            checked_seats += 1
            count += input_configuration[check_position] == 'L'
    return checked_seats == count

def is_seat_undesirable(input_configuration, position):
    count = 0
    for check_position in neighbours(position):
        if check_position in input_configuration:
            count += input_configuration[check_position] == '#'
        if count >= 4:
            return True
    return False

def update_configuration(input_configuration):
    output_configuration = input_configuration.copy()
    for position, occupancy in input_configuration.items():
        # take seat if desireable
        if occupancy == 'L' and is_seat_desirable(input_configuration, position):
            output_configuration[position] = '#'
        # leave seat if undesirable
        if occupancy == '#' and is_seat_undesirable(input_configuration,position):
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
