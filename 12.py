

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

# part 1
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

# part 2 waypoints

waypoint = (10, 1)
ship = (0,0)
current_location = (0,0)

def get_distance(current, waypoint):
    return tuple(waypoint[i] for i in range(2))


ROTATION = {
    'L': 1j,
    'R': -1j
}

for instruction in instructions:
    command, amount = instruction[0], int(instruction[1:])

    if command == 'R' or command == 'L':
        temp_x, temp_y = waypoint
        temp_waypoint= complex(temp_x, temp_y)
        count = amount // 90
        for c in range (count):
            temp_waypoint *= ROTATION[command]
        
        waypoint = (temp_waypoint.real, temp_waypoint.imag)
  

    global_direction = get_direction(absolute_index)

    if command in orientation_vector:
        waypoint = tuple(waypoint[i] + orientation_vector[command][i] * amount for i in range(2))
    print(waypoint)

    # move the ship
    if command == 'F':
        current_location = tuple(current_location[i] + amount*waypoint[i] for i in range(2))
        #waypoint = tuple(waypoint[i] + current_location[i] for i in range(2))

    print(command, ' loc', current_location, 'relative waypoint:', waypoint)
 
print(manhattan_distance(current_location)) # 39140
