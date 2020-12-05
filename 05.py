with open('inputs/05') as inputfile:
    boarding_passes = inputfile.readlines()

def code_to_binary(code):
    code = code.replace('R','1').replace('B','1').replace('F','0').replace('L','0')
    return(code)

def get_seat_position(code):
    row = code_to_binary(code[:7])
    column = code_to_binary(code [-3:])
    return(int(row,2), int(column,2))

part_1 = 0
all_seats = []
for boarding_pass in boarding_passes:
    boarding_pass = boarding_pass.strip()
    row, column = get_seat_position(boarding_pass)
    part_1 = max(part_1,  row*8 + column)
    all_seats.append(row*8 + column)

print(part_1)
all_seats.sort()
for i in range(len(all_seats)-1):
    if all_seats[i + 1] - all_seats[i] == 2:
        print(all_seats[i] + 1 )