

def get_direction(absolute_index):
    SIDES = ['E','S','W','N']
    absolute_index = absolute_index % 4
    return SIDES[absolute_index]

ORIENTATION_VECTOR = {
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'N': (0, 1)
}

def manhattan_distance(coordinate):
    return sum(abs(p) for p in coordinate)

# open and parse input
with open('./inputs/12', 'r') as infile:
    instructions = infile.readlines()

instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

# initial conditions part 1
absolute_index = 0
current_location = (0,0)

# part 1
for command, amount in instructions:

    # rotate ship orientation
    if command == 'R':
        absolute_index += amount // 90
    if command == 'L':
        absolute_index -= amount // 90
    global_direction = get_direction(absolute_index)

    # move the ship backward or forward (this is relative to orientation)
    if command == 'F':
        current_location = tuple(current_location[i] + ORIENTATION_VECTOR[global_direction][i] * amount for i in range(2))
    if command == 'B':
        current_location = tuple(current_location[i] - ORIENTATION_VECTOR[global_direction][i] * amount for i in range(2))

    # move the ship in absolute (E, S, W, or N) direction
    if command in ORIENTATION_VECTOR:
        current_location = tuple(current_location[i] + ORIENTATION_VECTOR[command][i] * amount for i in range(2))

print(f'Ship distance after following all the instructions is: {manhattan_distance(current_location)}')
# Ship distance after following all the instructions is: 858


# part 2 inital conditions
waypoint = (10, 1)
current_location = (0,0)

ROTATION = {
    'L': 1j,
    'R': -1j
}

# part 2
for command, amount in instructions:

    # rotate the waypoint (relative to the ship)
    if command == 'R' or command == 'L':
        temp_x, temp_y = waypoint
        temp_waypoint= complex(temp_x, temp_y)
        count = amount // 90
        for c in range (count):
            temp_waypoint *= ROTATION[command]
        
        waypoint = (int(temp_waypoint.real), int(temp_waypoint.imag))

    global_direction = get_direction(absolute_index)
    
    # move the waypoint (relative to the ship)
    if command in ORIENTATION_VECTOR:
        waypoint = tuple(waypoint[i] + ORIENTATION_VECTOR[command][i] * amount for i in range(2))

    # move the ship
    if command == 'F':
        current_location = tuple(current_location[i] + amount*waypoint[i] for i in range(2))
 
print(f'Ship distance following new rules is: {manhattan_distance(current_location)}!') # 39140
# Ship distance following new rules is: 39140!
