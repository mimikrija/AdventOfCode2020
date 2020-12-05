with open('inputs/05') as inputfile:
    boarding_passes = inputfile.readlines()

#boarding_passes = [ int('R' == digit) for boarding_pass in boarding_passes for digit in boarding_pass ]
part_1 = 0
for boarding_pass in boarding_passes:
    row_binary = ''
    seat_binary = ''
    for digit in boarding_pass[:7]:
        row_binary += str(int('B' == digit))
    for digit in boarding_pass [-4:-1]: #strip line
        seat_binary += str(int('R' == digit))
    part_1 = max(part_1,  int(row_binary,2)*8+ int(seat_binary,2))
    #print(row_binary, int(row_binary,2), seat_binary, int(seat_binary,2), "id is", int(row_binary,2)*8+ int(seat_binary,2))

print(part_1)