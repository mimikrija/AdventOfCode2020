import re
with open('inputs/24-ex') as inputfile:
    inputs = inputfile.readlines()

HEX_DIRECTIONS = {
    'nw': (0, 1, -1),
    'ne': (1, 0, -1),
     'e': (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
     'w': (-1, 1, 0)
}

re_directions = re.compile(r'nw|ne|se|sw|e|w')

def hex_add(in_hex_a, in_hex_b):
    return tuple(coordinate_a + coordinate_b for coordinate_a, coordinate_b in zip(in_hex_a, in_hex_b))

instructions = [re.findall(re_directions, line) for line in inputs]

flipped_tiles = {}
for instruction in instructions:
    position = (0, 0, 0)
    for direction in instruction:
        position = hex_add(position, HEX_DIRECTIONS[direction])
    if position in flipped_tiles:
        flipped_tiles[position] = not flipped_tiles[position]
    else:
        flipped_tiles[position] = True

part_1 = sum(value for value in flipped_tiles.values())
print(part_1)
