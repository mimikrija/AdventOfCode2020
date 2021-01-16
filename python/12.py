# Day 12: Rain Risk

UNIT_VECTOR = {
    'E': 1 + 0j,
    'S': 0 - 1j,
    'W': -1 + 0j,
    'N': 0 + 1j
}

ROTATION = {
    'L': 1j,
    'R': -1j
}

def move_it(command, amount):
    # move the ship in absolute (E, S, W, or N) direction by amount
    return UNIT_VECTOR[command] * amount

def rotate_it(command, amount):
    # rotate in increments of 90 degrees (L, R)
    direction = 1 + 0j
    for _ in range (amount//90):
        direction *= ROTATION[command]
    return direction

def go_forward(direction, amount):
    return direction * amount

def manhattan_distance(coordinate):
    return int(sum(abs(p) for p in [coordinate.real, coordinate.imag]))

def solve(part, instructions, ship_direction = UNIT_VECTOR['E']):
    current_location = 0 + 0j

    for command, amount in instructions:
        # rotate ship/waypoint
        if command in ROTATION.keys():
            ship_direction *= rotate_it(command, amount)

        # move the ship/waypoint in absolute (E, S, W, or N) direction by amount
        if command in UNIT_VECTOR:
            if part == 'part 1':
                current_location += move_it(command, amount)
            else:
                ship_direction += move_it(command, amount)

        # move the ship forward (F) in the ship_direction/waypoint by amount
        if command == 'F':
            current_location += go_forward(ship_direction, amount)

    print(f'Ship distance after following all the {part} instructions is: {manhattan_distance(current_location)}!')

# open and parse input
with open('./inputs/12', 'r') as infile:
    instructions = infile.readlines()
instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

solve('part 1', instructions)
solve('part 2', instructions, 10 + 1j)
# Ship distance after following all the part 1 instructions is: 858!
# Ship distance after following all the part 2 instructions is: 39140!
