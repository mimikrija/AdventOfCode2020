# Day 5: Binary Boarding

with open('inputs/05') as inputfile:
    boarding_passes = inputfile.readlines()

def code_to_binary(code):
    code = code.translate(str.maketrans('RBFL','1100'))
    return(code)

def get_seat_position(code):
    row = code_to_binary(code[:7])
    column = code_to_binary(code [-3:])
    return(int(row,2), int(column,2))

def seat_ID(code):
    row, column = get_seat_position(code)
    return row*8 + column
    # this could have been just: return code_to_binary(code)

def find_my_seat(input_list):
    list_of_seats = sorted(input_list)
    for i in range(len(list_of_seats)-1):
        if list_of_seats[i + 1] - list_of_seats[i] == 2:
            return list_of_seats[i] + 1


selected_seats = [seat_ID(boarding_pass.strip()) for boarding_pass in boarding_passes]

part_1 = max(selected_seats)
part_2 = find_my_seat(selected_seats)

print(f'The highest seat ID is {part_1}!')
print(f'My seat ID is: {part_2}!')
# The highest seat ID is 826!
# My seat ID is: 678!
