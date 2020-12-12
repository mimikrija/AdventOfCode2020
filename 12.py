

def get_direction(absolute_index):
    sides = ['E','S','W','N']
    absolute_index = absolute_index % 4
    return sides[absolute_index]

orientation_vector = {
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'N': (0, 1)
}

def manhattan_distance(coordinate):
    return sum(abs(p) for p in coordinate)

with open('./inputs/12', 'r') as infile:
    instructions = infile.readlines()

absolute_index = 0
current_location = (0,0)

for instruction in instructions:
    command, amount = instruction[0], int(instruction[1:])

    if command == 'R':
        absolute_index += amount // 90
    if command == 'L':
        absolute_index -= amount // 90

    global_direction = get_direction(absolute_index)

    if command == 'F':
        current_location = tuple(current_location[i] + orientation_vector[global_direction][i] * amount for i in range(2))
    if command == 'B':
        current_location = tuple(current_location[i] - orientation_vector[global_direction][i] * amount for i in range(2))

    if command in orientation_vector:
        current_location = tuple(current_location[i] + orientation_vector[command][i] * amount for i in range(2))


print(manhattan_distance(current_location)) # 858
