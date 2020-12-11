import copy

def neighbours(row_pos, seat_pos):
    return [(check_row, check_seat)
        for check_row in range (row_pos-1, row_pos + 2) for check_seat in range (seat_pos-1, seat_pos+2)
        if (check_row != row_pos or check_seat != seat_pos)
        and 0 <= check_row < total_rows and 0 <= check_seat < total_seats]

def is_seat_desirable(input_configuration,row_pos,seat_pos):
    count = 0
    checked_seats = 0
    for check_x, check_y in neighbours(row_pos, seat_pos):
        checked_seats += input_configuration[check_x][check_y] != '.'
        count += input_configuration[check_x][check_y] == 'L'
    return checked_seats == count

def is_seat_undesirable(input_configuration,row_pos,seat_pos):
    count = 0
    checked_seats = 0
    for check_x, check_y in neighbours(row_pos, seat_pos):
        count += input_configuration[check_x][check_y] == '#'
        if count >= 4:
            return True
    return False


def update_configuration(input_configuration):
    output_configuration = copy.deepcopy(input_configuration)
    for row_pos in range(0, total_rows):
        for seat_pos in range(0, total_seats):
            # take seat if desireable
            if input_configuration[row_pos][seat_pos] == 'L' and is_seat_desirable(input_configuration,row_pos,seat_pos):
                output_configuration[row_pos][seat_pos] = '#'
            # leave seat if undesirable
            if input_configuration[row_pos][seat_pos] == '#' and is_seat_undesirable(input_configuration,row_pos,seat_pos):
                output_configuration[row_pos][seat_pos] = 'L'
    return output_configuration

with open('inputs/11') as inputfile:
    rows = inputfile.readlines()

seat_configuration = []

for row in rows:
    row = row.strip()
    row = [c for c in row ]
    seat_configuration.append(row)

total_rows = len(seat_configuration)
total_seats = len(row)


next_configuration = []
while True:
    next_configuration = update_configuration(seat_configuration)
    if next_configuration == seat_configuration:
        break
    else:
        seat_configuration = copy.deepcopy(next_configuration)

part_1 = 0
for row in next_configuration:
    for seat in row:
        part_1 += seat == '#'

print(part_1) # 2204
