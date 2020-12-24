import re
with open('inputs/24') as inputfile:
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

def hex_neighbor(in_hex, direction):
    return hex_add(in_hex, HEX_DIRECTIONS[direction])

def tile_neighbors(in_hex):
    return [hex_neighbor(in_hex, direction) for direction in HEX_DIRECTIONS]

def art_installation(in_floor):
    new_floor = in_floor.copy()
    expanded_floor = new_floor.copy()
    for tile in in_floor:
        # expand mesh
        neighbors = tile_neighbors(tile)
        for neighbor in neighbors:
            if neighbor in expanded_floor:
                continue
            else:
                expanded_floor[neighbor] = False

    for tile, black in expanded_floor.items():
        neighbors = tile_neighbors(tile)
        count_black_adjacents = sum(expanded_floor.get(candidate, False) for candidate in neighbors)
        
        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        if black:
            if count_black_adjacents == 0 or count_black_adjacents > 2:
                new_floor[tile] = False
        # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        else:
            if count_black_adjacents == 2:
                new_floor[tile] = True


    return new_floor

def count_black_tiles(in_floor):
    return sum(black for black in in_floor.values())

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

part_1 = count_black_tiles(flipped_tiles)
print(f'After all the flipping, {part_1} tiles are left black side up!')
# After all the flipping, 469 tiles are left black side up!

current_floor = flipped_tiles.copy()


for day in range(1, 101):
    current_floor = art_installation(current_floor)

print(count_black_tiles(current_floor)) # 4353
