import re
from math import sqrt

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

def read_sides(in_tile):
    """ reads each side of `in_tile` from left to right and
    returns a list of four tiles """
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

def compare_tiles(ID_fixed, ID_possible_match, tiles_dict):
    """ checks if any of the sides in `ID_fixed` mathes with any
    of the sides in possible configurations of `ID_possible_match`"""
    sides_to_look_at = tiles_dict[ID_fixed][0]
    for sides in tiles_dict[ID_possible_match]:
        for side in sides:
            if side in sides_to_look_at:
                return True
    return False


# read input from file
re_numbers = re.compile(r'\d+')
inputs = open('inputs/20').read().split('\n\n')

# define tile/final image constants
NUMBER_OF_TILES = len(inputs)
IMAGE_SIDE_SIZE = int(sqrt(NUMBER_OF_TILES))
TILE_SIZE = len(inputs[0].split('\n')[0])

# parse input into dict of tiles {ID: actual tile image from input file
# with '#' converted to '1' and '.' converted to '0'}
input_tiles = {}
for tile in inputs:
    tile_data = tile.split('\n')
    ID = int(re.findall(re_numbers, tile_data[0])[0])
    tile_rows = tile_data[1:]
    tile_array = [[str(int(column == '#')) for column in row] for row in tile_rows]
    input_tiles[ID] = tile_array

# generate a dictionary which maps tile IDs to a list of possible configurations,
# where possible configurations are lists of slide numbers, and slide numbers flipped
tiles_sides_only = { ID: [convert_sides_to_num(sides) for sides in generate_configurations(read_sides(tile))] for ID, tile in input_tiles.items() }


# generate a dictionary of matched tiles:
# {ID: set of matching tiles}
matched_tiles = {}
for ID_to_compare_to in tiles_sides_only.keys():
    for candidate_ID in tiles_sides_only.keys():
        if candidate_ID == ID_to_compare_to:
            continue
        else:
            if compare_tiles(ID_to_compare_to, candidate_ID, tiles_sides_only):
                if ID_to_compare_to in matched_tiles:
                    matched_tiles[ID_to_compare_to].add(candidate_ID)
                else:
                    matched_tiles[ID_to_compare_to] = set([candidate_ID])


# split matched tiles into three different categories
corners = {}
borders = {}
middles = {}
for tile, match in matched_tiles.items():
    if len (match) == 2:   # corners
        corners[tile] = match
    elif len (match) == 3: # borders
        borders[tile] = match
    else:                  # middles
        middles[tile] = match

# party 1 solution: multiply IDs of corner tiles
party_1 = 1
for tile in corners:
    party_1 *= tile

print(f'Multiplied corner IDs: {" * ".join(str(tile) for tile in corners)} = {party_1}!')
# Multiplied corner IDs: 1867 * 2441 * 2633 * 1663 = 19955159604613!
