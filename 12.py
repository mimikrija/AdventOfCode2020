UNIT_VECTOR = {
    'E': 1 + 0j,
    'S': 0 - 1j,
    'W': -1 + 0j,
    'N': 0 + 1j
}

DIRECTION_FACTORS = {
    'F': 1,
    'B': -1
}

ROTATION = {
    'L': 1j,
    'R': -1j
}

def manhattan_distance(coordinate):
    return int(sum(abs(p) for p in [coordinate.real, coordinate.imag]))

# open and parse input
with open('./inputs/12', 'r') as infile:
    instructions = infile.readlines()

instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

# initial conditions part 1

current_location = 0 + 0j
ship_direction = UNIT_VECTOR['E']

# part 1
for command, amount in instructions:

    # rotate ship in increments of 90 degrees (L, R)
    if command in ROTATION.keys():
        for _ in range (amount//90):
            ship_direction *= ROTATION[command]

    # move the ship backward or forward (B, F) in the ship_direction by amount
    if command in DIRECTION_FACTORS.keys():
        current_location += DIRECTION_FACTORS[command] * ship_direction * amount

    # move the ship in absolute (E, S, W, or N) direction by amount
    if command in UNIT_VECTOR:
        current_location += UNIT_VECTOR[command] * amount

print(f'Ship distance after following all the instructions is: {manhattan_distance(current_location)}!')
# Ship distance after following all the instructions is: 858!


# part 2 inital conditions
waypoint = 10 + 1j
current_location = 0 + 0j

# part 2
for command, amount in instructions:
    # waypoint is always relative to the ship location!

    # rotate waypoint in increments of 90 degrees (L, R)
    if command in ROTATION.keys():
        for _ in range (amount//90):
            waypoint *= ROTATION[command]

    # move the waypoint in absolute (E, S, W, or N) direction by amount
    if command in UNIT_VECTOR:
        waypoint += UNIT_VECTOR[command] * amount

    # move the in the waypoint direction by amount
    if command == 'F':
        current_location += waypoint * amount
 
print(f'Ship distance following new rules is: {manhattan_distance(current_location)}!') # 39140
# Ship distance following new rules is: 39140!
