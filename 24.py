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
    new_floor = {}
    expanded_floor = {tile: black for tile, black in in_floor.items() if black}
    for tile in in_floor:
        # expand mesh
        neighbors = tile_neighbors(tile)
        for neighbor in neighbors:
            expanded_floor[neighbor] = in_floor.get(neighbor, False)

    # LOOP THROUGH EXPANDED MESH OTHERWISE THERE IS REALLY NO POINT OF EXPANDING IS IT?!
    for tile, black in expanded_floor.items():
        neighbors = tile_neighbors(tile)
        count_black_adjacents = sum(expanded_floor.get(candidate, False) for candidate in neighbors)
        
        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white
        # else it remains the same (black) and needs to remain in the dictionary as black hence the `not`
        if black:
            new_floor[tile] = not (count_black_adjacents == 0 or count_black_adjacents > 2)

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

days_of_art = 100
for day in range(100):
    current_floor = art_installation(current_floor)
part_2 = count_black_tiles(current_floor)

print(f'After {days_of_art} days of art installation, there are {part_2} black tiles in the lobby!')
# After 100 days of art installation, there are 4353 black tiles in the lobby!