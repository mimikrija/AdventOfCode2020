with open('inputs/05') as inputfile:
    boarding_passes = inputfile.readlines()

def code_to_binary(code):
    code = code.replace('R','1').replace('B','1').replace('F','0').replace('L','0')
    return(code)

part_1 = 0
all_seats = []
for boarding_pass in boarding_passes:
    boarding_pass = boarding_pass.strip()
    row_binary = code_to_binary(boarding_pass[:7])
    seat_binary = code_to_binary(boarding_pass [-3:])

    part_1 = max(part_1,  int(row_binary,2)*8+ int(seat_binary,2))
    all_seats.append(int(row_binary,2)*8+ int(seat_binary,2))

print(part_1)
all_seats.sort()
for i in range(len(all_seats)-1):
    if all_seats[i + 1] - all_seats[i] == 2:
        print(all_seats[i] + 1 )