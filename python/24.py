# Day 24: Lobby Layout

import re

HEX_DIRECTIONS = {
    'nw': (0, 1, -1),
    'ne': (1, 0, -1),
     'e': (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
     'w': (-1, 1, 0)
}


def hex_add(in_hex_a, in_hex_b):
    return tuple(coordinate_a + coordinate_b for coordinate_a, coordinate_b in zip(in_hex_a, in_hex_b))

def hex_neighbor(in_hex, direction):
    return hex_add(in_hex, HEX_DIRECTIONS[direction])

def tile_neighbors(in_hex):
    return {hex_neighbor(in_hex, direction) for direction in HEX_DIRECTIONS}

def art_installation(in_black_tiles):
    out_black_tiles = set()
    relevant_white_tiles = set()
    for tile in in_black_tiles:
        relevant_white_tiles |= {neighbor for neighbor in tile_neighbors(tile) if neighbor not in in_black_tiles}

    for tile in in_black_tiles | relevant_white_tiles:
        neighbors = tile_neighbors(tile)
        count_black_adjacents = sum(neighbor in in_black_tiles for neighbor in neighbors)
        if (tile in in_black_tiles and 0 < count_black_adjacents <= 2) or (tile in relevant_white_tiles and count_black_adjacents == 2):
            out_black_tiles.add(tile)

    return out_black_tiles

# read and parse input into u a set of black tiles positions
with open('inputs/24') as inputfile:
    inputs = inputfile.readlines()

re_directions = re.compile(r'nw|ne|se|sw|e|w') 

black_tiles = set()
for instruction in (re.findall(re_directions, line) for line in inputs):
    position = (0, 0, 0)
    for direction in instruction:
        position = hex_add(position, HEX_DIRECTIONS[direction])
    black_tiles ^= {position}


part_1 = len(black_tiles)
print(f'After all the flipping, {part_1} tiles are left black side up!')
# After all the flipping, 469 tiles are left black side up!

days_of_art = 100
for day in range(days_of_art):
    black_tiles = art_installation(black_tiles)
part_2 = len(black_tiles)

print(f'After {days_of_art} days of art installation, there are {part_2} black tiles in the lobby!')
# After 100 days of art installation, there are 4353 black tiles in the lobby!
