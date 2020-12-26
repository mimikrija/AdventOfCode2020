import re

def convert_sides_to_num(in_sides):
    return [int(side,2) for side in in_sides]

def generate_configurations(in_sides):
    # there are 4 possible configurations: original/rotated, flipped horizontally, flipped vertically, fliped both
    # flipped both reduces to rotation, so we don't care about that one
    # flipped vertically and flipped horizontally differ only by two rotations
    # the property of any flipped configuration is that *ALL* the sides are reversed (and their order is reversed as well)
    # the property of any non-flipped configuration is that *ALL* the sides are not reversed.
    # hence (for matching purposes) it is enough to generate a list of sides and a list of flipped sides
    flipped = reversed([''.join(reversed(side)) for side in in_sides])

    return [in_sides, flipped]

re_numbers = re.compile(r'\d+')
inputs = open('inputs/20').read().split('\n\n')
input_tiles = {}

NUMBER_OF_TILES = len(inputs)
TILE_SIZE = len(inputs[0].split('\n')[0])

for tile in inputs:
    tile_data = tile.split('\n')
    ID = re.findall(re_numbers, tile_data[0])[0]
    tile_rows = tile_data[1:]
    #tile_array = [row for row in tile_rows]
    #tile_array = [ convert_side_to_num(row) for row in tile_rows]
    tile_array = [[str(int(column == '#')) for column in row] for row in tile_rows]
    input_tiles[ID] = tile_array

def read_sides(in_tile):
    columns = list(zip(*in_tile))
    side_W = list(columns[0])
    side_E = list(columns[TILE_SIZE-1])
    side_W.reverse()
    side_N = in_tile[0]
    side_S = in_tile[TILE_SIZE-1]
    side_S.reverse()
    sides = [side_N, side_E, side_S, side_W]
    sides = [''.join(side) for side in sides]
    return sides

tiles_sides_only = {}


for ID, tile in input_tiles.items():
    tile_sides_binary = read_sides(tile)
    bla = generate_configurations(tile_sides_binary)
    tile_slides_dec = [convert_sides_to_num(sides) for sides in generate_configurations(tile_sides_binary)]
    tiles_sides_only[ID] = tile_slides_dec # {elem for sides in tile_slides_dec for elem in sides}


matched_tiles = {}

def compare_tiles(ID_fixed, ID_possible_match, tiles_dict):
    sides_to_look_at = tiles_dict[ID_fixed][0]
    for sides in tiles_dict[ID_possible_match]:
        for side in sides:
            if side in sides_to_look_at:
                return True
    return False

for compare_with in tiles_sides_only.keys():
    for ID, tile in tiles_sides_only.items():
        if ID == compare_with:
            continue
        else:
            if compare_tiles(ID, compare_with, tiles_sides_only):
                if compare_with in matched_tiles:
                    matched_tiles[compare_with].add(ID)
                else:
                    matched_tiles[compare_with] = set([ID])
corners = {}
borders = {}
middles = {}

party_1 = 1
for tile, match in matched_tiles.items():
    if len (match) == 2:   # corners
        corners[tile] = match
    elif len (match) == 3: # borders
        borders[tile] = match
    else:                  # middles
        middles[tile] = match

for tile in corners:
    party_1 *= int(tile)

print(f'Multiplied corner IDs: {" * ".join(tile for tile in corners)} = {party_1}!')
# Multiplied corner IDs: 1867 * 2441 * 2633 * 1663 = 19955159604613!

